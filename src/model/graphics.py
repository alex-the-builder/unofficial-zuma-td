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