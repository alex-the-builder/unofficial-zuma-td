import pyxel
from src.model.player import Player
from src.model.shooter import Shooter
from src.model.bullet import Bullet
from src.model.enemy import Enemy
from src.model.path import Path
from src.model.cell import Cell, CellType
from src.model.game_settings import GameSettings, load_settings
from src.model.shooter import Shooter, Direction
from src.model.tower import Tower
from src.model.game_state import GameState

TILE_SIZE = 16
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 240
FPS = 30

class GameController:
    def __init__(self):
        self.settings: GameSettings = load_settings()
        self.player = Player(lives=self.settings.lives)
        self._setup_path()
        self.shooter = Shooter(
            x=SCREEN_WIDTH // 2,
            y=SCREEN_HEIGHT // 2,
            colors=[8,11]
        )
        self.bullets: list[Bullet] = []
        self.enemies: list[Enemy] = []
        self.spawn_queue: list[Enemy] = self._spawn_enemies(self.settings.enemies_per_round)
        self.spawn_timer: float = 0.0
        self.spawn_delay: float = 2.0
        self.current_round: int = 1
        self.total_rounds: int = 2
        self.state: GameState = GameState.PLAYING
        self.towers: list[Tower] = []

    def _setup_path(self) -> None:
        cells: list[Cell] = []

        # horizontal segment: row 2, col 0 to 10
        for col in range(11):
            cell_type = CellType.SPAWN if col == 0 else CellType.PATH
            cells.append(Cell(row=2, col=col, cell_type=cell_type))

        # vertical segment: col 10, row 3 to 12
        for row in range(3, 13):
            cell_type = CellType.GOAL if row == 12 else CellType.PATH
            cells.append(Cell(row=row, col=10, cell_type=cell_type))

        self.path = Path(cells)

    def _spawn_enemies(self, count: int) -> list[Enemy]:
        import random
        colors = [8, 11]
        return [Enemy(color=random.choice(colors), hp=1, speed=2.0, path=self.path) for _ in range(count)]
    
    def _start_next_round(self) -> None:
        self.current_round += 1
        self.spawn_queue = self._spawn_enemies(self.settings.enemies_per_round)
        self.spawn_timer = 0.0
        self.state = GameState.PLAYING
    
    def update(self) -> None:
        dt = 1.0 / FPS

        match self.state:
            case GameState.PLAYING:
                self._update_playing(dt)
            case GameState.PLACE_TOWER:
                self._update_place_tower()
            case GameState.GAME_OVER:
                self._update_game_over()
            case _:
                pass

    def _update_playing(self, dt: float) -> None:
        # check round over
        all_spawned = len(self.spawn_queue) == 0
        all_dead = len(self.enemies) == 0
        if all_spawned and all_dead:
            if self.current_round >= self.total_rounds:
                self.state = GameState.GAME_OVER
            else:
                # self.sfx_round_end()
                self.state = GameState.PLACE_TOWER

        if not self.player.is_alive():
            self.state = GameState.GAME_OVER

        self.spawn_timer += dt
        if self.spawn_queue and self.spawn_timer >= self.spawn_delay:
            self.spawn_timer = 0.0
            self.enemies.append(self.spawn_queue.pop(0))

        self.shooter.update(dt)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.shooter.ready_to_fire:
            self._shoot()
            self.shooter.reset_fire()

        for bullet in self.bullets:
            bullet.update(dt)

        for enemy in self.enemies:
            enemy.update(dt)

        for tower in self.towers:
            tower.update(dt)
            if tower.ready_to_fire():
                self.bullets.append(tower.shoot())

        self._check_collisions()
        self._check_goal()

        self.bullets = [b for b in self.bullets if b.active and not b.is_out_of_bounds(SCREEN_WIDTH, SCREEN_HEIGHT)]
        self.enemies = [e for e in self.enemies if e.alive]

    def _update_game_over(self) -> None:
        if pyxel.btnp(pyxel.KEY_R):
            self.__init__()

    def _update_place_tower(self) -> None:
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self._try_place_tower()
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._start_next_round()

    def _try_place_tower(self) -> None:
        import random
        if self.player.exp >= 5:
            mx = pyxel.mouse_x
            my = pyxel.mouse_y
            self.player.exp -= 5
            self.towers.append(Tower(x=mx, y=my, color=random.choice([8, 11])))

    """
    def _handle_input(self) -> None:
        import pyxel
        if pyxel.btn(pyxel.KEY_W):
            self.shooter.direction = Direction.UP
        elif pyxel.btn(pyxel.KEY_S):
            self.shooter.direction = Direction.DOWN
        elif pyxel.btn(pyxel.KEY_A):
            self.shooter.direction = Direction.LEFT
        elif pyxel.btn(pyxel.KEY_D):
            self.shooter.direction = Direction.RIGHT
    """

    def _shoot(self) -> None:
        dx, dy = self.shooter.get_direction_vector(SCREEN_WIDTH, SCREEN_HEIGHT, pyxel.mouse_x, pyxel.mouse_y)
        color = self.shooter.get_next_color()
        bullet = Bullet(
            x=float(self.shooter.x),
            y=float(self.shooter.y),
            dx=dx,
            dy=dy,
            color=color,
            speed=48.0
        )
        self.bullets.append(bullet)

    def _check_collisions(self) -> None:
        for bullet in self.bullets:
            for enemy in self.enemies:
                if not bullet.active or not enemy.alive:
                    continue
                if bullet.hits(enemy.x, enemy.y, TILE_SIZE):
                    if enemy.take_hit(bullet.color):
                        ...
                    bullet.active = False
                    if not enemy.alive:
                        self.player.gain_exp(1)

    def _check_goal(self) -> None:
        for enemy in self.enemies:
            if enemy.reached_goal:
                self.player.lose_life()

    def draw(self) -> None:
        # always draw path and towers
        for cell in self.path.cells:
            pyxel.rect(cell.col * TILE_SIZE, cell.row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 5)

        for tower in self.towers:
            pyxel.rect(tower.x - 8, tower.y - 8, TILE_SIZE, TILE_SIZE, 10)

        match self.state:
            case GameState.PLAYING:
                self._draw_playing()
            case GameState.PLACE_TOWER:
                self._draw_place_tower()
            case GameState.GAME_OVER:
                self._draw_game_over()
            case _:
                pass

    def _draw_playing(self) -> None:
        for enemy in self.enemies:
            pyxel.rect(enemy.x, enemy.y, TILE_SIZE, TILE_SIZE, enemy.color)

        for bullet in self.bullets:
            pyxel.circ(int(bullet.x), int(bullet.y), bullet.radius, bullet.color)

        pyxel.rect(self.shooter.x - 8, self.shooter.y - 8, TILE_SIZE, TILE_SIZE, 11)

        pyxel.text(4, 4, f"LIVES: {self.player.lives}", 7)
        pyxel.text(4, 12, f"EXP: {self.player.exp}", 7)

    def _draw_place_tower(self) -> None:
        pyxel.text(70, 100, f"ROUND {self.current_round} COMPLETE", 7)
        pyxel.text(55, 110, "CLICK TO PLACE TOWER (5 EXP)", 7)
        pyxel.text(65, 120, "PRESS ENTER TO CONTINUE", 7)
        pyxel.text(4, 4, f"EXP: {self.player.exp}", 7)

    def _draw_game_over(self) -> None:
        pyxel.text(90, 110, "GAME OVER", 8)
        pyxel.text(75, 120, "PRESS R TO RESTART", 7)