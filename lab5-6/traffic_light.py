from state import Red
from singleton_meta import SingletonMeta


class TrafficLight(metaclass=SingletonMeta):
    def __init__(self):
        self.state = Red()

    def set_state(self, state):
        self.state = state

    def change_state(self):
        self.state.next(self)

    def get_state(self):
        return str(self.state)
