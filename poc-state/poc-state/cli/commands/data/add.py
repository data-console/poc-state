import click
from cli.commands.commons import pass_data_product, not_implemented
from cli.model import DataProduct
from cli.model.data import SQL


@click.command('source')
def add_source():
    not_implemented()


@click.command('result')
def add_result():
    not_implemented()


@click.command('sql')
@click.option('--name', '-n', prompt='Provide unique SQL query name', help='SQL query name')
@click.option('file_name', '--file', required=False, help='SQL file location')
@click.option('saved_query', '--from-bigquery', required=False, help='BigQuery saved query reference')
@pass_data_product
def add_sql(data_product: DataProduct, name: str, file_name, saved_query=None):
    data_product.data.add_sql(SQL(name, file_name or f'data/sqls/{name}.sql', saved_query))


@click.command(name='notebook')
def add_notebook():
    not_implemented()


@click.command(name='dbt')
def add_dbt():
    not_implemented()


@click.group()
def add():
    pass


add.add_command(add_source)
add.add_command(add_result)
add.add_command(add_sql)
add.add_command(add_notebook)
add.add_command(add_dbt)
