from random import choice
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        pass

    def choose_name(self):
        self.name = input("Enter computer name: ")
        pass    

    def choose_gesture(self):
        self.chosen_gesture = choice(self.gestures)
        print(f'{self.name} throws {self.chosen_gesture}.')
        pass      
    
    
