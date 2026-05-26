class Player:
    def __init__(self, lives: int):
        self.lives = lives
        self.exp: int = 0

    def lose_life(self) -> None:
        self.lives -= 1

    def gain_exp(self, amount: int) -> None:
        self.exp += amount

    def is_alive(self) -> bool:
        return self.lives > 0