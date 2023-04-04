from typing import Any
from typing import Optional

from cookiecutter.cli import cookiecutter
from rich import print
from rich.pretty import Pretty
from rich.panel import Panel
from topwing.project_builder import ProjectBuilderEngine


class CookiecutterEngine(ProjectBuilderEngine):

    def list_templates(self) -> None:
        print(Panel(
            Pretty(
                self._configuration.templates, indent_guides=True
            ),
            title="Available templates"
        ))

    def create(
        self,
        template_tag: str,
        cvs_init: bool=False,
        csv_server_init: bool=False,
        checkout: Optional[str]=None,
        extra_context: list[str] = [],
        no_input: bool=False,
        replay: Optional[str]=None,
        overwrite_if_exists: bool=False,
        output_dir: str='.',
        config_file: Optional[str]=None,
        default_config: bool=False,
        password: Optional[str]=None,
        directory: Optional[str]=None,
        skip_if_file_exists: bool=False,
        accept_hooks: bool=True,
    ) -> Any:
        result_path = cookiecutter(
            self._configuration.templates.get(template_tag, template_tag),
            checkout=checkout or self._configuration.options.checkout,
            no_input=no_input or self._configuration.options.no_input,
            extra_context=self._parse_extra_context(extra_context) | self._configuration.options.extra_context,
            replay=replay or self._configuration.options.replay,
            overwrite_if_exists=overwrite_if_exists or self._configuration.options.overwrite_if_exists,
            output_dir=output_dir or self._configuration.options.output_dir,
            config_file=config_file or self._configuration.options.config_file,
            default_config=default_config or self._configuration.options.default_config,
            password=password or self._configuration.options.password,
            directory=directory or self._configuration.options.directory,
            skip_if_file_exists=skip_if_file_exists or self._configuration.options.skip_if_file_exists,
            accept_hooks=accept_hooks or self._configuration.options.accept_hooks,
        )
        if cvs_init:
            ...
        if cvs_init and csv_server_init:
            ...
        return result_path

    @staticmethod
    def _parse_extra_context(extra_context: list[str]) -> dict[str, str]:
        return {
            key: value
            for key, value in map(
                lambda context: str.split(context, '='),
                extra_context,
            )
        }
