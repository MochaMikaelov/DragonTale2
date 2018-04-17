from gameOver import GameOver
from level1 import Level1
from menu import Menu


class Manager:

    def __init__(self):
        self.states = [
            GameOver(),
            Menu(self),
            Level1(self)
        ]
        self.state_index = 1

    def update(self):
        self.states[self.state_index].update()

    def draw(self, display):
        self.states[self.state_index].draw(display)

    def key_pressed(self, key):
        self.states[self.state_index].key_pressed(key)

    def key_released(self, key):
        self.states[self.state_index].key_released(key)
