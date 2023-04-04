from importlib.metadata import entry_points
from importlib.metadata import EntryPoint


class Registry:

    def __init__(self) -> None:
        self.__registry__: dict[str, EntryPoint] = {}

    def register(self, key: str, obj: EntryPoint) -> None:
        self.__registry__[key] = obj

    def retrieve(self, tag):
        return self.__registry__[tag].load()


def register(entry_point_name: str):
    registry = Registry()
    for entry_point in entry_points(group=entry_point_name):
        registry.register(entry_point.name, entry_point)
    return registry
