import pyxel
from src.controller.game_controller import GameController

class App:
    def __init__(self):
        pyxel.init(240, 240, title="Zuma: Tower Defense", fps=30)
        self.controller = GameController()
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.controller.update()

    def draw(self):
        pyxel.cls(0)
        self.controller.draw()

App()