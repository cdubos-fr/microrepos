from abc import ABC
from abc import abstractmethod


class CVSManager(ABC):

    @abstractmethod
    def clone(self):...

    @abstractmethod
    def pull(self):...

    @abstractmethod
    def update_local(self):...

    @abstractmethod
    def update_remote(self):...

    @abstractmethod
    def diff(self):...

    @abstractmethod
    def change_branch(self):...

    @abstractmethod
    def apply_changes(self):...

    @abstractmethod
    def revert_changes(self):...
