import click


@click.command()
def delete_source():
    pass


@click.command()
def delete_result():
    pass


@click.command()
def delete_sql():
    pass


@click.command()
def delete_notebook():
    pass


@click.group()
def delete():
    pass


delete.add_command(delete_source)
delete.add_command(delete_result)
delete.add_command(delete_notebook)
delete.add_command(delete_sql)
