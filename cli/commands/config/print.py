import click
import yaml

from cli.commands.commons import pass_data_product
from cli.model.data_product import DataProduct


@click.command(name='print')
@pass_data_product
def print_config(data_product: DataProduct):
    click.echo(yaml.dump(data_product.serialize()))
