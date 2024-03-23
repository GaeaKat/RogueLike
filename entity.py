from __future__ import annotations
import copy
from typing import Optional, Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap
T = TypeVar("T", bound="Entity")



class Entity:
    """
    A generic object to represent players, enemies, items etc
    """

    gamemap: GameMap
    def __init__(self,
                 gamemap: Optional[GameMap] = None,
                 x: int = 0,
                 y: int = 0,
                 char: str = "?",
                 color: Tuple[int, int, int] = (255, 255, 255),
                 name: str = "<Unnamed>",
                 blocks_movement: bool = False):
        self.x = int(x)
        self.y = int(y)
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """
        Spawn a copy of this instance at the given location.
        :param gamemap: Dungeon game map
        :param x: x coordinate
        :param y: y coordinate
        :return: copy of this
        """
        clone = copy.deepcopy(self)
        clone.x = int(x)
        clone.y = int(y)
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x:int, y: int,gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location.  Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "gamemap"):
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            self.gamemap.entities.add(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
