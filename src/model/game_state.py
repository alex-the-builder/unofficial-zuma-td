from enum import auto, StrEnum

class GameState(StrEnum):
    START_MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    PLACE_TOWER = auto()
    GAME_OVER = auto()
    LEADERBOARD = auto()