from src.model.bullet import Bullet

class Tower:
    def __init__(self, x: int, y: int, color: int, fire_rate: float = 0.5):
        self.x = x
        self.y = y
        self.color = color
        self.fire_rate = fire_rate
        self.fire_timer: float = 0.0
        self.cost: int = 5

    def update(self, dt: float) -> None:
        self.fire_timer += dt

    def ready_to_fire(self) -> bool:
        return self.fire_timer >= 1.0 / self.fire_rate

    def shoot(self) -> Bullet:
        self.fire_timer = 0.0
        return Bullet(
            x=float(self.x),
            y=float(self.y),
            dx=0.0,
            dy=-1.0,
            color=self.color,
            speed=48.0
        )