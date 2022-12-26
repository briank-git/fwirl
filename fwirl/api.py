import pendulum as plm
from coolname import generate_slug
from .message import get_msg, publish_msg, listen

def summarize(graph_key, rabbit_url = __RABBIT_URL__):
    resp_name = 'summarize-'+generate_slug(2)
    publish_msg(graph_key, {"type": "summarize", "resp_queue": resp_name}, rabbit_url) 
    queue = []
    get_msg(resp_name, queue, rabbit_url)
    print(queue[0])

def ls(graph_key, assets = False, schedules = False, jobs = False, rabbit_url = __RABBIT_URL__):
    resp_name = 'ls-'+generate_slug(2)
    publish_msg(graph_key, {"type": "ls", "resp_queue": resp_name, "assets" : assets, "schedules" : schedules, "jobs" : jobs}, rabbit_url) 
    queue = []
    get_msg(resp_name, queue, rabbit_url)
    print(queue[0])

def refresh(graph_key, asset_key = None, rabbit_url = __RABBIT_URL__):
    publish_msg(graph_key, {"type": "refresh", "asset_key" : asset_key}, rabbit_url)

def build(graph_key, asset_key = None, rabbit_url = __RABBIT_URL__):
    publish_msg(graph_key, {"type": "build", "asset_key" : asset_key}, rabbit_url)

def pause(graph_key, key=None, rabbit_url = __RABBIT_URL__):
    publish_msg(graph_key, {"type": "pause", "key" : key}, rabbit_url)

def unpause(graph_key, key=None, rabbit_url = __RABBIT_URL__):
    publish_msg(graph_key, {"type": "unpause", "key" : key}, rabbit_url)
    
def schedule(graph_key, schedule_key, action, cron_str, asset_key=None, rabbit_url = __RABBIT_URL__):
    publish_msg(graph_key, {"type": "schedule", "schedule_key" : schedule_key, "action" : action, "cron_str" : cron_str, "asset_key" : asset_key}, rabbit_url)
    
def unschedule(graph_key, schedule_key, rabbit_url = __RABBIT_URL__):
    publish_msg(graph_key, {"type": "unschedule", "schedule_key" : schedule_key}, rabbit_url)
    
# TODO cancel job
