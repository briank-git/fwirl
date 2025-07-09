import asyncio
import threading
from aiohttp import web
import os, sys
import tempfile
import glob
import psutil
from loguru import logger

SERVERPORT = 8081

def aiohttp_server():
    def handle_request(request):
        graph_id = request.match_info['graph_id']
        return web.Response(text=f"Graph ID: {graph_id}")

    app = web.Application()
    app.add_routes([web.get('/graphs/{graph_id}', handle_request)])
    runner = web.AppRunner(app)
    return runner


def run_server(runner):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, '127.0.0.1', SERVERPORT)
    loop.run_until_complete(site.start())
    loop.run_forever()

def start_webserver():
    fpid = os.fork()
    if fpid != 0:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, prefix='fwirlserverpid_', dir=tempfile.gettempdir()) as temp_file:
            temp_file.write(str(fpid))
        sys.exit(0)

    logger.info(f"Starting webserver on port {SERVERPORT}...")
    t = threading.Thread(target=run_server, args=(aiohttp_server(),))
    t.start()
        
def stop_webserver():
    temp_dir = tempfile.gettempdir()
    pid_files = glob.glob(os.path.join(temp_dir, 'fwirlserverpid_*'))

    logger.info("Stopping webserver...")

    for pid_file in pid_files:
        try:
            with open(pid_file, 'r') as temp_file:
                pid = int(temp_file.read().strip())
        except:
            pid = None

        if pid is None:
            continue

        try:
            process = psutil.Process(pid)
            process.terminate() 
            process.wait(timeout=10)

            os.unlink(pid_file)
        except psutil.TimeoutExpired:
            logger.info(f"Failed to stop webserver process {pid}, timeout expired.")
        except psutil.AccessDenied:
            logger.info(f"Failed to stop webserver process {pid}, access denied.")
        except:
            pass






