import json
from dataclasses import dataclass

@dataclass
class GameSettings:
    lives: int
    enemies_per_round: int
    regen_distance: int
    chameleon_frequency: int

def load_settings(path: str = "settings.json") -> GameSettings:
    with open(path, "r") as f:
        data = json.load(f)
    return GameSettings(
        lives=data["lives"],
        enemies_per_round=data["enemies_per_round"],
        regen_distance=data["regen_distance"],
        chameleon_frequency=data["chameleon_frequency"]
    )