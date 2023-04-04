from typing import Any
from collections.abc import Sequence
from abc import ABC
from abc import abstractmethod


class CVSServerManager(ABC):

    @abstractmethod
    def get_repo(self, repo_name: str, url: str) -> str:
        ...

    @abstractmethod
    def search_repos(self, *args: Any, **kwargs: Any) -> Sequence[str]:
        ...
