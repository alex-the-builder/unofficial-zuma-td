import pyxel
from abc import ABC, abstractmethod

class BaseGraphics(ABC):
    @abstractmethod
    def __init__(self, x: int, y: int, width: int, length: int):
        ...

class BaseTile(BaseGraphics):
    def __init__(self, x: int, y: int, width: int, length: int):
        pyxel.blt(x, y, 1, 48, 0, width, length)

class GrassTile(BaseGraphics):
    def __init__(self, x: int, y: int, width: int, length: int):
        pyxel.blt(x, y, 1, 32, 0, width, length)

class FlowerTile(BaseGraphics):
    def __init__(self, x: int, y: int, width: int, length: int):
        pyxel.blt(x, y, 1, 64, 0, width, length)

class PathTile(BaseGraphics):
    def __init__(self, x: int, y: int, width: int, length: int):
        pyxel.blt(x, y, 1, 16, 0, width, length)

class TunnelTile(BaseGraphics):
    def __init__(self, x: int, y: int, width: int, length: int):
        pyxel.blt(x, y, 1, 0, 0, width, length)

class NormalEnemy(BaseGraphics):
    normal_enemy = {
        8: (0 ,0),
        11: (16, 0),
        2: (32, 0),
        9: (0, 16),
        14: (16, 16),
        15: (32, 16)
    }

    def __init__(self, x: int, y: int, width: int, length: int, color: int):
        pyxel.blt(x, y, 0, self.normal_enemy[color][0], self.normal_enemy[color][1], width, length)