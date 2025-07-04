import click
from .api import (
                 summarize as api_summarize,
                 ls as api_ls,
                 refresh as api_refresh,
                 build as api_build,
                 pause as api_pause,
                 unpause as api_unpause,
                 schedule as api_schedule,
                 unschedule as api_unschedule,
                 shutdown as api_shutdown
                )
from .message import __RABBIT_URL__

@click.group()
def cli():
    pass

@click.command()
@click.argument("graph")
@click.option("--rabbit_url", default=__RABBIT_URL__)
def summarize(graph, rabbit_url):
    api_summarize(graph, rabbit_url)
cli.add_command(summarize)

@click.command()
@click.argument("graph")
@click.option("--rabbit_url", default=__RABBIT_URL__)
def shutdown(graph, rabbit_url):
    api_shutdown(graph, rabbit_url)
cli.add_command(shutdown)

@click.command()
@click.argument("graph")
@click.option("--assets", is_flag=True, default=False)
@click.option("--schedules", is_flag=True, default=False)
@click.option("--jobs", is_flag=True, default=False)
@click.option("--rabbit_url", default=__RABBIT_URL__)
def ls(graph, assets, schedules, jobs, rabbit_url):
    api_ls(graph, assets, schedules, jobs, rabbit_url)
cli.add_command(ls)

@click.command()
@click.argument("graph")
@click.option("--asset", default=None)
@click.option("--rabbit_url", default=__RABBIT_URL__)
def refresh(graph, asset, rabbit_url):
    api_refresh(graph, asset, rabbit_url)
cli.add_command(refresh)

@click.command()
@click.argument("graph")
@click.option("--asset", default=None)
@click.option("--rabbit_url", default=__RABBIT_URL__)
def build(graph, asset, rabbit_url):
    api_build(graph, asset, rabbit_url)
cli.add_command(build)

@click.command()
@click.argument("graph")
@click.argument("key")
@click.option("--rabbit_url", default=__RABBIT_URL__)
def pause(graph, key, rabbit_url):
    api_pause(graph, key, rabbit_url)
cli.add_command(pause)

@click.command()
@click.argument("graph")
@click.argument("key")
@click.option("--rabbit_url", default=__RABBIT_URL__)
def unpause(graph, key, rabbit_url):
    api_unpause(graph, key, rabbit_url)
cli.add_command(unpause)

@click.command()
@click.argument("graph")
@click.argument("schedule")
@click.argument("action")
@click.argument("cron_string")
@click.option("--asset", default=None)
@click.option("--rabbit_url", default=__RABBIT_URL__)
def schedule(graph, schedule, action, cron_string, asset, rabbit_url):
    api_schedule(graph, schedule, action, cron_string, asset, rabbit_url)
cli.add_command(schedule)

@click.command()
@click.argument("graph")
@click.argument("schedule")
@click.option("--rabbit_url", default=__RABBIT_URL__)
def unschedule(graph, schedule, rabbit_url):
    api_unschedule(graph, schedule, rabbit_url)
cli.add_command(unschedule)

