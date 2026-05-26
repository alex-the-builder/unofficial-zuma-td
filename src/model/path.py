from src.model.cell import Cell

class Path:
    def __init__(self, cells: list[Cell]):
        self.cells = cells

    def get_next_cell(self, index: int) -> Cell | None:
        if index + 1 < len(self.cells):
            return self.cells[index + 1]
        return None  

    def get_spawn(self) -> Cell:
        return self.cells[0]

    def get_goal(self) -> Cell:
        return self.cells[-1]