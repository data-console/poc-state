import abc
import textwrap
import abc
import typing


class Entity(abc.ABC):

    def __init__(self, kind, name, **kwargs):
        self._kind = kind
        self._name = name
        self._description = kwargs.pop('description')
        self._spec = self.generate_spec(**kwargs)

    def to_dict(self):
        return {
            'apiVersion': 'backstage.io/v1alpha1',
            'kind': self._kind,
            'metadata': {
                'name': self._name,
                'description': self._description,
                'namespace': 'default'
            },
            'spec': self._spec
        }

    @classmethod
    @abc.abstractmethod
    def generate_spec(cls, **kwargs):
        pass


class Component(Entity):

    def __init__(self, name, **kwargs):
        super().__init__('Component',
                         name=f'{kwargs["component_type"]}-{name}',
                         description=kwargs.pop('description', name),
                         component_type=kwargs.pop('component_type'),
                         **kwargs)

    @classmethod
    def generate_spec(cls, component_type, owner='unknown', lifecycle='experimental'):
        return {
          'type': component_type,
          'lifecycle': lifecycle,
          'owner': owner
        }


class Resource(Entity):

    def __init__(self, name, resource_type, **kwargs):
        super().__init__('Resource',
                         name=f'{resource_type}-{name}',
                         desription=kwargs.pop('description', name),
                         resource_type=resource_type,
                         **kwargs)

    @classmethod
    def generate_spec(cls, resource_type, owner):
        return {
          'type': resource_type,
          'owner': owner
        }


class CatalogEntityProvider(abc.ABC):

    @abc.abstractmethod
    def to_catalog_entities(self) -> typing.List[Entity]:
        pass
