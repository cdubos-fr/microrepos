from typing import Any
from typing import Literal
from typing import Optional

from pydantic import BaseSettings
import yaml
import os
import platform
from .exceptions import NoConfigfileException
from pydantic.env_settings import SettingsSourceCallable
from pydantic import Field


class ProjectBuilderOptions(BaseSettings):
    checkout: Optional[str]=None
    no_input: bool=False
    extra_context: dict[str, str] = {}
    replay: Optional[str]=None
    overwrite_if_exists: bool=False
    output_dir: str='.'
    config_file: Optional[str]=None
    default_config: bool=False
    password: Optional[str]=None
    directory: Optional[str]=None
    skip_if_file_exists: bool=False
    accept_hooks: bool=True
    init_git: bool=False


class ProjectBuilderSetting(BaseSettings):
    engine: str = 'cookiecutter'
    options: ProjectBuilderOptions = ProjectBuilderOptions()
    templates: dict[str, str]



def get_home_config_from_system() -> Literal['UserProfile', 'HOME']:
    if platform.system() == 'Windows':
        env = os.environ['UserProfile']
    else:
        env = os.environ['HOME']
    return env


def yaml_settings_source(settings: "TopWingSettings") -> dict[str, Any]:
    basedirs = [get_home_config_from_system()]
    if venv := os.environ.get('VIRTUAL_ENV'):
        basedirs.insert(0, os.path.dirname(venv))

    for basedir in basedirs:
        configfile = os.path.join(basedir, settings.__config__.configfile)
        if os.path.exists(configfile):
            with open(configfile) as f:
                return yaml.load(f, Loader=yaml.SafeLoader) or {}

    raise NoConfigfileException('Configuration file not found')

import warnings
with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)

    class TopWingSettings(BaseSettings):
        project_builder: ProjectBuilderSetting = Field(alias='project-builder')

        class Config:
            env_prefix = 'topwing_'
            case_sensitive = False
            configfile = '.topwing.yaml'
            allow_population_by_field_name = True

            @classmethod
            def customise_sources(
                cls,
                init_settings: SettingsSourceCallable,
                env_settings: SettingsSourceCallable,
                file_secret_settings: SettingsSourceCallable,
            ):
                return (
                    init_settings,
                    yaml_settings_source,
                    env_settings,
                    file_secret_settings,
                )
