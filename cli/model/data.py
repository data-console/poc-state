import typing
from .base import Entry, Registry, Serializable


class SQL(Entry):
    pass


class SQLRegistry(Registry):

    @classmethod
    def load_entry(cls, config: typing.Any):
        return SQL.load(config)


class Data(Serializable):

    def __init__(self, sqls=None):
        self._sqls = sqls or SQLRegistry()

    @property
    def sqls(self) -> SQLRegistry:
        return self._sqls

    def add_sql(self, sql: SQL):
        self._sqls.add_entry(sql)

    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        return {'sqls': self.sqls.serialize()}

    @classmethod
    def load(cls, config: typing.Any):
        return cls(sqls=SQLRegistry.load(config['sqls']))
