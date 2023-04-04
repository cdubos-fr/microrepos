from pydantic import BaseSettings


class Engine:
    __commands__: tuple[str, ...]

    def __init__(self, configuration: BaseSettings) -> None:
        self._configuration = configuration
