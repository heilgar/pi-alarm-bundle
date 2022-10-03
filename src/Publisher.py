from .Status import Status
from abc import abstractmethod


class Publisher:
    def __init__(self, status: Status):
        self._status = status

    def notify(self, status: bool):
        self._status.state = status

    @abstractmethod
    def publish_status(self, args: list | None = None) -> None:
        pass
