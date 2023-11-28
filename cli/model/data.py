class DataProductException(Exception):
    pass


class Serializable:

    def serialize(self):
        pass


class Entry:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def to_dict(self) -> dict[str, str]:
        return {'name': self._name}


class Registry:

    def __init__(self, entries: list[Entry] = None):
        self._existing_entries = entries or []
        self._new_entries = []

    @property
    def entries(self):
        return self._existing_entries + self._new_entries

    def __contains__(self, item: Entry):
        return any(item.name == entry.name for entry in self.entries)

    def add_entry(self, entry: Entry):
        if entry in self:
            raise DataProductException(f"entry with name: {entry.name} already exists")
        self._new_entries.append(entry)

    def to_list(self) -> list[dict[str, str]]:
        return [entry.to_dict() for entry in self.entries]


class SQL(Entry):
    pass


class SQLRegistry(Registry):
    pass


class Data:

    def __inii__(self):
        self._sqls = SQLRegistry()

    @property
    def sqls(self) -> SQLRegistry:
        return self._sqls

    def add_sql(self, sql: SQL):
        self._sqls.add_entry(sql)
