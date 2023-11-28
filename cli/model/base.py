import abc
import typing


class DataProductException(Exception):
    pass


class Serializable(abc.ABC):

    @abc.abstractmethod
    def serialize(self) -> typing.Union[dict[str, typing.Any], list[typing.Any]]:
        pass

    @classmethod
    @abc.abstractmethod
    def load(cls, config: typing.Any):
        pass


class Entry(Serializable):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def serialize(self) -> dict[str, str]:
        return {'name': self._name}

    @classmethod
    def load(cls, config: typing.Any):
        if 'name' not in config:
            raise AttributeError('missing name attribute')
        return cls(config['name'])


class Registry(Serializable):

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

    def serialize(self) -> list[dict[str, str]]:
        return [entry.serialize() for entry in self.entries]

    @classmethod
    def load(cls, config: typing.Any):
        return cls([cls.load_entry(entry_config) for entry_config in config])

    @classmethod
    @abc.abstractmethod
    def load_entry(cls, config: typing.Any):
        pass
