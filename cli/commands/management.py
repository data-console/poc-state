import sys

import click


@click.command()
def check():
    sys.exit(1)


@click.group()
def publish():
    pass
