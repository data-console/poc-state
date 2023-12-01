import typing
import yaml

from cli.model.data import Data
from cli.model.base import Serializable
from cli.model.catalog_info import CatalogEntityProvider, Entity, Component


class Pipelines(Serializable, CatalogEntityProvider):

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {}

    def to_catalog_entities(self, **kwargs) -> typing.List[Entity]:
        return []

    @classmethod
    def load(cls, config: typing.Any):
        return cls()


class Infra(Serializable, CatalogEntityProvider):

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {}

    def to_catalog_entities(self, **kwargs) -> typing.List[Entity]:
        return []

    @classmethod
    def load(cls, config: typing.Any):
        return cls()


class ML(Serializable, CatalogEntityProvider):

    def to_catalog_entities(self, **kwargs) -> typing.List[Entity]:
        return []

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {}

    @classmethod
    def load(cls, config: typing.Any):
        return cls()


class DataProduct(Serializable, CatalogEntityProvider):

    def __init__(self, name: str, description: str, data: Data = None, pipelines: Pipelines = None, infra: Infra = None, ml: ML = None):
        self._name = name
        self._description = description
        self._data = data or Data()
        self._pipelines = pipelines or Pipelines()
        self._infra = infra or Infra()
        self._ml = ml or ML()

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def data(self) -> Data:
        return self._data

    @property
    def pipelines(self) -> Pipelines:
        return self._pipelines

    @property
    def infra(self) -> Infra:
        return self._infra

    @property
    def ml(self) -> ML:
        return self._ml

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {
            'name': self.name,
            'description': self.description,
            'data': self.data.serialize(),
            'pipelines': self.pipelines.serialize(),
            'infra': self.infra.serialize(),
            'ml': self.ml.serialize()
        }

    def to_catalog_entities(self, **kwargs) -> typing.List[Entity]:
        return ([Component(name=self.name, description=self.description, component_type='data-product', **kwargs)]
                + self.data.to_catalog_entities(**kwargs)
                + self.pipelines.to_catalog_entities(**kwargs)
                + self.ml.to_catalog_entities(**kwargs)
                + self.infra.to_catalog_entities(**kwargs))

    @classmethod
    def load(cls, config: dict[str, typing.Any]):
        return DataProduct(
            name=config['name'],
            description=config['description'],
            data=Data.load(config['data']),
            ml=ML.load(config['ml']),
            pipelines=Pipelines.load(config['pipelines']),
            infra=Infra.load(config['infra']))
