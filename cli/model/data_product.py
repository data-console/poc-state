from cli.model.data import Data


class Pipelines:
    pass


class Infra:
    pass


class ML:
    pass


class DataProduct:

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

    @classmethod
    def from_config(cls, config_dir):
        return DataProduct()
