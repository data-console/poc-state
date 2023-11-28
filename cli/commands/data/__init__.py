import click
from .add import add
from .delete import delete
from .list import list_data
from .show import show
from.infer import infer


@click.group()
def data():
    pass


data.add_command(add)
data.add_command(delete)
data.add_command(show)
data.add_command(list_data)
data.add_command(infer)
