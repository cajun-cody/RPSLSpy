from AI import AI
from human import Human

class Game:
    def __init__(self) -> None:
        self.player_one = Human()
        self.player_two = None
        pass

    def run_game(self):
        self.welcome_greeting()
        self.game_type()
        self.game_round()
        self.game_winner()

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
        print('Best of 3 Wins!\n')

    # Choose to play with another Human, the AI or AI vs AI
    def game_type(self):
        game_type = int(input("Choose game type: (1) Player vs Player or (2) Player vs AI or (3) AI vs AI?  "))
        if game_type == 1:
            self.player_one = Human()
            self.player_two = Human()
            self.player_one.choose_name()
            self.player_two.choose_name()
            print(f"Player 1's name is {self.player_one.name}.")
            print(f"Player 2's name is {self.player_two.name}.")

        elif game_type == 2:
            self.player_one = Human()
            self.player_two = AI()
            self.player_one.choose_name()
            self.player_two.choose_name()
            print(f"Player 1's name is {self.player_one.name}.")
            print(f"Player 2's name is {self.player_two.name}.")

        elif game_type == 3:
            self.player_one = AI()
            self.player_two = AI()
            self.player_one.choose_name()
            self.player_two.choose_name()
            print(f"Player 1's name is {self.player_one.name}.")
            print(f"Player 2's name is {self.player_two.name}.")
    
    # While loop to run through each round with either 1 point added for a win or 0 points for tie. Loop ends 
    # when one player reaches 2 points. 
    def game_round(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            print('\nNew Round\n')
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("Round Tied!")

            elif self.player_one.chosen_gesture == self.player_one.gestures[0] and self.player_two.chosen_gesture == self.player_two.gestures[2]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
                
            elif self.player_one.chosen_gesture == self.player_one.gestures[1] and self.player_two.chosen_gesture == self.player_two.gestures[0]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
                
            elif self.player_one.chosen_gesture == self.player_one.gestures[2] and self.player_two.chosen_gesture == self.player_two.gestures[1]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
                
            elif self.player_one.chosen_gesture == self.player_one.gestures[3] and self.player_two.chosen_gesture == self.player_two.gestures[4]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
                
            elif self.player_one.chosen_gesture == self.player_one.gestures[4] and self.player_two.chosen_gesture == self.player_two.gestures[2]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
                
            elif self.player_one.chosen_gesture == self.player_one.gestures[0] and self.player_two.chosen_gesture == self.player_two.gestures[3]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
                
            elif self.player_one.chosen_gesture == self.player_one.gestures[1] and self.player_two.chosen_gesture == self.player_two.gestures[4]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
                
            elif self.player_one.chosen_gesture == self.player_one.gestures[2] and self.player_two.chosen_gesture == self.player_two.gestures[3]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")

            elif self.player_one.chosen_gesture == self.player_one.gestures[3] and self.player_two.chosen_gesture == self.player_two.gestures[1]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")

            elif self.player_one.chosen_gesture == self.player_one.gestures[4] and self.player_two.chosen_gesture == self.player_two.gestures[0]:
                self.player_one.score += 1
                print(f"{self.player_one.name} wins round.")
            
            else:
                self.player_two.score += 1
                print(f"{self.player_two.name} wins round.")

    # Winner decided when one player reaches 2 points.       
    def game_winner(self):
        if self.player_one.score >= 2:
            print(f"\n{self.player_one.name.title()} Wins Game!")
        elif self.player_two.score >= 2:
            print(f"\n{self.player_two.name.title()} Wins Game!")

   