class Status:
    def __init__(self, state: bool = False):
        self._state = state
        self._observers = []

    def notify(self):
        """Alert the observers"""
        for observer in self._observers:
            observer.update(self)

    def attach(self, observer):

        """If the observer is not in the list,
        append it into the list"""

        if observer not in self._observers:
            self._observers.append(observer)

    @property
    def state(self) -> bool:
        return self._state

    @state.setter
    def state(self, state: bool):
        if self._state != state:
            self._state = state
            self.notify()
