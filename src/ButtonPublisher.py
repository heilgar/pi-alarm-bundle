from .Publisher import Publisher
from .Status import Status
from datetime import datetime


class ButtonPublisher(Publisher):
    _pressed: datetime | None = None

    def __init__(self, status: Status):
        Publisher.__init__(self, status)

    def publish_status(self, channel: list | None = None) -> None:
        now = datetime.now()

        if self._pressed is None:
            self._pressed = now
            self.notify(True)

        if self._pressed is not None:
            diff = (now - self._pressed).total_seconds() / 60
            if diff > 1.0:
                self._pressed = None
                self.notify(False)
