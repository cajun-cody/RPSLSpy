from AI import AI
from human import Human

class Game:
    def __init__(self) -> None:
        self.player_one = Human()
        self.player_two = AI()
        pass

