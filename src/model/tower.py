from src.model.bullet import Bullet
from src.model.shooter import Shooter, DoubleShot
from src.model.direction import *
from typing import Protocol
class Tower(Protocol):
    x:int
    y:int
    shooter:Shooter
    color:int
    cost:int
    upgrade_cost:int
    def upgrade(self) -> Tower | None:
        ...
    def change_dir(self,dir:Direction) -> None:
        ...

class SimpleTowerLVL1:
    def __init__(self, x:int,y:int, shooter:Shooter):
        self.x = x
        self.y = y
        self.shooter = shooter
        self.color:int = 10
        self.cost: int = 5
        self.upgrade_cost:int = 3
    def upgrade(self) -> Tower | None:
        return SimpleTowerLVL2(x=self.x,y=self.y,shooter=self.shooter)
    def change_dir(self,dir:Direction) -> None:
        self.shooter.direction = dir
    #handle upgrade inside or outside

class SimpleTowerLVL2(SimpleTowerLVL1):
    def __init__(self, x:int,y:int, shooter:Shooter):
        self.x = x
        self.y = y
        self.shooter = shooter
        self.color:int = 10
        self.cost: int = 5
        self.upgrade_cost:int = 3
    def upgrade(self) -> Tower | None:
        return None
    def change_dir(self,dir:Direction) -> None:
        self.shooter.direction = dir