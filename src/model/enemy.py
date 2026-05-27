from src.model.cell import Cell
from src.model.path import Path

class Enemy:
    def __init__(self, color: int, hp: int, speed: float, path: Path):
        self.color = color
        self.hp = hp
        self.speed = speed
        self.path = path
        self.path_index: int = 0
        self.x: int
        self.y: int
        self.x, self.y = self._get_spawn_coords()
        self.alive: bool = True
        self.reached_goal: bool = False
        self.move_timer: float = 0.0

    def _get_spawn_coords(self) -> tuple[int, int]:
        spawn: Cell = self.path.get_spawn()
        return spawn.col * 16, spawn.row * 16

    def take_hit(self, bullet_color: int) -> bool:
        if bullet_color == self.color:
            self.hp -= 1
            if self.hp <= 0:
                self.alive = False
                return True
        return False

    def move(self) -> None:
        next_cell: Cell | None = self.path.get_next_cell(self.path_index)
        if next_cell is None:
            self.reached_goal = True
            self.alive = False
            return
        self.path_index += 1
        self.x = next_cell.col * 16
        self.y = next_cell.row * 16

    def update(self, dt: float) -> None:
        if not self.alive:
            return
        self.move_timer += dt
        if self.move_timer >= self.speed:
            self.move_timer = 0.0
            self.move()