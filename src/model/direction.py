from typing import Protocol
import math
import pyxel
class Direction(Protocol):
    def get_direction_vector(self,x:float,y:float) -> tuple[float,float]:
        ...
class UpDirection:
    def get_direction_vector(self,x:float,y:float) -> tuple[float,float]:
        return (0.0, -1.0)

class DownDirection:
    def get_direction_vector(self,x:float,y:float) -> tuple[float,float]:
        return (0.0, 1.0)

class LeftDirection:
    def get_direction_vector(self,x:float,y:float) -> tuple[float,float]:
        return (-1.0, 0.0)

class RightDirection:
    def get_direction_vector(self,x:float,y:float) -> tuple[float,float]:
        return (1.0, 0.0)

class MouseDirection:
    def get_direction_vector(self,x:float,y:float) -> tuple[float,float]:
        mouse_x = pyxel.mouse_x
        mouse_y = pyxel.mouse_y
        a = x - mouse_x
        b = y - mouse_y
        t = math.atan2(b, a)
        return (-math.cos(t), -math.sin(t))