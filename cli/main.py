import click
import pathlib
from cli.commands import data, ml, check, infra, publish, pipeline
from cli.model.data_product import DataProduct


@click.group()
@click.option('--config',
              help='Data Product configuration directory',
              envvar='DATA_PRODUCT_HOME',
              default='.dp',
              type=click.Path(path_type=pathlib.Path, file_okay=False, dir_okay=True, exists=True, writable=True, readable=True))
@click.pass_context
def main(ctx, config):
    """Data Product CLI which governs Allegro's data product state."""
    ctx.obj = DataProduct.from_config(config)
    click.echo(f"loading context from: {config}")


main.add_command(infra)
main.add_command(data)
main.add_command(ml)
main.add_command(pipeline)
main.add_command(publish)
main.add_command(check)


if __name__ == '__main__':
    main()
