import random
from src.model.direction import Direction
from src.model.bullet import Bullet
from typing import Protocol
class ShotPattern(Protocol):
    def get_next_color(self,colors:list[int]) -> int:
        """Given a list of integers representing the available colors,
            return one random color"""
        return random.choice(colors)
    def spawn_bullets(self,x:int,y:int,dx:float,dy:float,colors:list[int]) -> list[Bullet]:
        """Given the position of the shooter and the direction of the bullets, 
            spawn n bullets"""
        ...
class SingleShot:
    def get_next_color(self,colors:list[int]) -> int:
        """Given a list of integers representing the available colors,
            return one random color"""
        return random.choice(colors)
    def spawn_bullets(self,x:int,y:int,dx:float,dy:float,colors:list[int]) -> list[Bullet]:
        bullet = Bullet(
            x=float(x),
            y=float(y),
            dx=dx,
            dy=dy,
            color=self.get_next_color(colors),
            speed=48.0
        )
        return [bullet]
class DoubleShot:
    def get_next_color(self,colors:list[int]) -> int:
        """Given a list of integers representing the available colors,
            return one random color"""
        return random.choice(colors)
    def spawn_bullets(self,x:int,y:int,dx:float,dy:float,colors:list[int]) -> list[Bullet]:
        b1 = Bullet(
            x=float(x)+2.5,
            y=float(y),
            dx=dx,
            dy=dy,
            color=self.get_next_color(colors),
            speed=48.0
        )
        b2 = Bullet(
            x=float(x)+2.5,
            y=float(y),
            dx=dx,
            dy=dy,
            color=self.get_next_color(colors),
            speed=48.0
        )
        return [b1,b2]
class Shooter:
    def __init__(self, x: int, y: int, direction:Direction, fire_rate:float, colors: list[int]):
        self.x = x
        self.y = y
        self.fire_rate = fire_rate
        self.direction = direction
        self.colors = colors
        self.current_color: int = colors[0]
        self.fire_rate: float = 0.9
        self.fire_timer: float = 0.0
        self.ready_to_fire: bool = False
        self.shot_pattern:ShotPattern = SingleShot()

    def update(self, dt: float) -> None:
        self.fire_timer += dt
        if self.fire_timer >= 1.0 / self.fire_rate:
            self.fire_timer = 0.0
            self.ready_to_fire = True
    def shoot(self, x:int, y:int) -> list[Bullet]:
        dx, dy = self.direction.get_direction_vector(self.x,self.y)
        bullets = self.shot_pattern.spawn_bullets(x,y,dx,dy,self.colors)
        return bullets

    def reset_fire(self) -> None:
        self.ready_to_fire = False