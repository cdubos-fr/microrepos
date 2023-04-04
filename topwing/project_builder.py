from typing import Any
from typing import Callable
from typing import cast
from abc import ABC
from abc import abstractmethod


from topwing.config import TopWingSettings
from topwing.config import ProjectBuilderSetting

from .engine import Engine
from .registry import register



project_builder_registry = register("project-builder")


class ProjectBuilderEngine(Engine, ABC):
    __commands__= ('list_templates', 'create')
    _configuration: ProjectBuilderSetting

    def __init__(self, configuration: ProjectBuilderSetting) -> None:
        super().__init__(configuration)

    @abstractmethod
    def list_templates(self) -> None:
        ...

    @abstractmethod
    def create(self, *args: Any, cvs_init: bool=False, csv_server_init: bool=False, **kwargs: Any) -> Any:
        ...


def get_commands() -> list[Callable[..., Any]]:
    config = TopWingSettings().project_builder
    engine = cast(Engine, project_builder_registry.retrieve(config.engine)(config))
    return [getattr(engine, cmd) for cmd in engine.__commands__]
