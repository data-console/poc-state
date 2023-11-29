import click
import yaml

from cli.commands.commons import pass_data_product
from cli.model.data_product import DataProduct


@click.command(name='catalog-info')
@click.option('--output', '-o', type=click.File('w', encoding='utf-8'), default=click.get_text_stream('stdout'))
@click.option('--release-version', '-r', default='snapshot')
@pass_data_product
def generate_catalog_info(data_product: DataProduct, output: click.File, release_version: str):
    yaml.dump_all([entity.to_dict() for entity in data_product.to_catalog_entities(version=release_version)], output, default_flow_style=False)
