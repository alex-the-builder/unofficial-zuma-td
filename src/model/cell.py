from enum import auto, StrEnum

class CellType(StrEnum):
    EMPTY = auto()
    PATH = auto()
    TUNNEL = auto()
    SPAWN = auto()
    GOAL = auto()
    TOWER = auto()

class Cell:
    def __init__(self, row: int, col: int, cell_type: CellType = CellType.EMPTY):
        self.row = row
        self.col = col
        self.cell_type = cell_type