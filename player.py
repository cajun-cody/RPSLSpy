


class Player:
    def __init__(self) -> None:
        self.name = ''
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = ''
        self.score = 0
        pass

    
    def choose_name(self):
        self.name = input("Enter player name: ")
        pass


    def choose_gesture(self):
        chosen_gesture = input(f'Choose your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, {self.gestures[4]}')
        if chosen_gesture in self.gestures:
            self.chosen_gesture = chosen_gesture
            print(f'{self.name} throws {self.chosen_gesture}.')
        else:
            self.choose_gesture()