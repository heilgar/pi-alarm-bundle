from abc import abstractmethod
from .Status import Status
from play_audio import play_alarm, play_abort_alarm


class Observer:
    @abstractmethod
    def update(self, status: Status) -> None:
        """
        Receive update from subject.
        """
        pass


class StatusObserver(Observer):
    def update(self, status: Status):
        print('Observed state: ' + str(status.state))
        if status.state:
            play_alarm()
        else:
            play_abort_alarm()
