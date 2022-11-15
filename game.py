from AI import AI
from human import Human

class Game:
    def __init__(self) -> None:
        self.player_one = Human()
        self.player_two = AI()
        pass

    def run_game(self):
        self.welcome_greeting()
        self.game_type()

    def welcome_greeting(self):
        print('\nWelcome to Rock, Paper, Scissors, Lizard, Spock!')
        print('Game Instructions Are:\n')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitate Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
        print('and as it always has,')
        print('Rock crushes Scissors\n')
      
    def game_type(self):
        game_type = int(input("Choose game type: (1) Player vs Player or (2) Player vs AI"))
        if game_type == 1:
            self.player_two = Human()
            self.player_one.choose_name()
            self.player_two.choose_name()
            print(f"Player 1's name is {self.player_one.name}.")
            print(f"Player 2's name is {self.player_two.name}.")
        else:
            game_type == 2
            self.player_two = AI()
            self.player_two.choose_name()
            self.player_one.choose_name()
            print(f"Player 1's name is {self.player_one.name}.")
            print(f"Player 2's name is {self.player_two.name}.")
   
    
    def game_round(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            print('New Round\n')
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("Round Tied!")
            elif self.player_one.chosen_gesture == self.player_one.chosen_gesture[0] and self.player_two.chosen_gesture == self.player_two.chosen_gesture[1]:
                print(f"{self.player_one.name} wins the round.")
            elif self.player_one.chosen_gesture == self.player_one.chosen_gesture[1] and self.player_two.chosen_gesture == self.player_two.chosen_gesture[2]:
                print(f"{self.player_one.name} wins the round.")

          


   