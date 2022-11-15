from random import choice
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = input("What would you like to name the computer? ")
        pass

    def choose_gesture(self):
        self.chosen_gesture = choice(self.gestures)
        print(f'{self.name} throws {self.chosen_gesture}.')
        pass      