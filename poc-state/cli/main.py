import click
import pathlib
import yaml

from cli.commands import data, ml, infra, pipeline, config
from cli.model.data_product import DataProduct


class DataProductContext:

    def __init__(self, config_dir):
        self._config_dir = config_dir
        self._data_product = None

    def __enter__(self):
        with open(f"{self._config_dir}/config.yaml", "r") as stream:
            config_file_content = yaml.safe_load(stream)
        self._data_product = DataProduct.load(config_file_content)
        return self._data_product

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(f"{self._config_dir}/config.yaml", 'w') as file:
            file.write(yaml.dump(self._data_product.serialize()))


@click.group()
@click.option('config_dir', '--config',
              help='Data Product configuration directory',
              envvar='DATA_PRODUCT_HOME',
              default='.dp',
              type=click.Path(path_type=pathlib.Path, file_okay=False, dir_okay=True, exists=True, writable=True, readable=True))
@click.pass_context
def main(ctx, config_dir):
    """Data Product CLI which governs Allegro's data product state."""
    ctx.obj = ctx.with_resource(DataProductContext(config_dir))


main.add_command(infra)
main.add_command(data)
main.add_command(ml)
main.add_command(pipeline)
main.add_command(config)


if __name__ == '__main__':
    main()
