import click
from cli.commands.config.print import print_config
from cli.commands.config.catalog_info import generate_catalog_info
from cli.commands.config.verify import verify


@click.group()
def config():
    pass


config.add_command(print_config)
config.add_command(generate_catalog_info)
config.add_command(verify)
