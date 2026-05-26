import math

class Bullet:
    def __init__(self, x: float, y: float, dx: float, dy: float, color: int, speed: float):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.speed = speed
        self.active: bool = True
        self.radius: int = 5

    def update(self, dt: float) -> None:
        if not self.active:
            return
        self.x += self.dx * self.speed * dt
        self.y += self.dy * self.speed * dt

    def is_out_of_bounds(self, width: int, height: int) -> bool:
        return (
            self.x < 0 or self.x > width or
            self.y < 0 or self.y > height
        )

    def hits(self, enemy_x: float, enemy_y: float, tile_size: int) -> bool:
        dist = math.sqrt((self.x - enemy_x) ** 2 + (self.y - enemy_y) ** 2)
        return dist < self.radius + tile_size // 2