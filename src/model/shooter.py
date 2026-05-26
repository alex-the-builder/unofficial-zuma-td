import random
from enum import auto, StrEnum

class Direction(StrEnum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class Shooter:
    def __init__(self, x: int, y: int, colors: list[int]):
        self.x = x
        self.y = y
        self.colors = colors
        self.current_color: int = colors[0]
        self.fire_rate: float = 0.9
        self.fire_timer: float = 0.0
        self.ready_to_fire: bool = False
        self.direction: Direction = Direction.UP

    def update(self, dt: float) -> None:
        self.fire_timer += dt
        if self.fire_timer >= 1.0 / self.fire_rate:
            self.fire_timer = 0.0
            self.ready_to_fire = True

    def get_next_color(self) -> int:
        return random.choice(self.colors)

    def reset_fire(self) -> None:
        self.ready_to_fire = False

    def get_direction_vector(self) -> tuple[float, float]:
        match self.direction:
            case Direction.UP:
                return 0.0, -1.0
            case Direction.DOWN:
                return 0.0, 1.0
            case Direction.LEFT:
                return -1.0, 0.0
            case Direction.RIGHT:
                return 1.0, 0.0