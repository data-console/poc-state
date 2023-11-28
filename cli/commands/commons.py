import click
from cli.model.data_product import DataProduct

pass_data_product = click.make_pass_decorator(DataProduct)

def not_implemented():
    raise click.get_current_context().fail("not implemented yet")
