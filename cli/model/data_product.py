import typing
import yaml

from cli.model.data import Data
from cli.model.base import Serializable


class Pipelines(Serializable):

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {}

    @classmethod
    def load(cls, config: typing.Any):
        return cls()


class Infra(Serializable):

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {}

    @classmethod
    def load(cls, config: typing.Any):
        return cls()


class ML(Serializable):

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {}

    @classmethod
    def load(cls, config: typing.Any):
        return cls()


class DataProduct(Serializable):

    def __init__(self, data: Data = None, pipelines: Pipelines = None, infra: Infra = None, ml: ML = None):
        self._data = data or Data()
        self._pipelines = pipelines or Pipelines()
        self._infra = infra or Infra()
        self._ml = ml or ML()

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
            'data': self.data.serialize(),
            'pipelines': self.pipelines.serialize(),
            'infra': self.infra.serialize(),
            'ml': self.ml.serialize()
        }

    @classmethod
    def load(cls, config: dict[str, typing.Any]):
        return DataProduct(
            data=Data.load(config['data']),
            ml=ML.load(config['ml']),
            pipelines=Pipelines.load(config['pipelines']),
            infra=Infra.load(config['infra']))
