from src.model.shooter import Shooter
class Player:
    def __init__(self, x:int, y:int, lives: int, shooter:Shooter):
        self.x = x
        self.y = y
        self.lives = lives
        self.exp: int = 0
        self.shooter = shooter

    def lose_life(self) -> None:
        self.lives -= 1

    def gain_exp(self, amount: int) -> None:
        self.exp += amount

    def is_alive(self) -> bool:
        return self.lives > 0