import click
from cli.commands.config.print import print_config


@click.group()
def config():
    pass


config.add_command(print_config)