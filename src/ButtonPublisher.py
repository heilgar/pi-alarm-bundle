from .Publisher import Publisher
from .Status import Status
from datetime import datetime
import RPi.GPIO as GPIO

class ButtonPublisher(Publisher):
    _pressed: datetime | None = None

    def __init__(self, status: Status):
        Publisher.__init__(self, status)

    def trigger_status(self):
        self.notify(not self._status.state)

    def publish_status(self, channel: list | None = None) -> None:
        now = datetime.now()
        state = GPIO.input(13)

        if state == 0:
            if self._pressed is None: 
                self._pressed = now
                self.trigger_status()

            diff = (now - self._pressed).total_seconds() / 60

            if diff > 1.0:
                self._pressed = now
                self.trigger_status()

