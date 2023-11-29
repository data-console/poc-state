import typing
from .base import Entry, Registry, Serializable
from .catalog_info import CatalogEntityProvider, Component, Entity


class SQL(Entry):

    def __init__(self, name, file_name, saved_query=None):
        super().__init__(name)
        self._file_name = file_name
        self._saved_query = saved_query

    @property
    def file_name(self):
        return self._file_name

    @property
    def saved_query(self):
        return self._saved_query

    def serialize(self) -> dict[str, str]:
        content = super().serialize()
        content['file_name'] = self.file_name
        if self.saved_query:
            content['saved_query'] = self.saved_query
        return content

    def to_catalog_entities(self) -> typing.List[Entity]:
        return [Component(name=self.name, component_type="sql-query")]


class SQLRegistry(Registry):

    @classmethod
    def load_entry(cls, config: typing.Any):
        return SQL.load(config)


class Data(Serializable, CatalogEntityProvider):

    def __init__(self, sqls=None):
        self._sqls = sqls or SQLRegistry()

    @property
    def sqls(self) -> SQLRegistry:
        return self._sqls

    def add_sql(self, sql: SQL):
        self._sqls.add_entry(sql)

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {'sqls': self.sqls.serialize()}

    def to_catalog_entities(self) -> typing.List[Entity]:
        return self._sqls.to_catalog_entities()

    @classmethod
    def load(cls, config: typing.Any):
        return cls(sqls=SQLRegistry.load(config['sqls']))
