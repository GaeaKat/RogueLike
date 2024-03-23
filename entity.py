from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items etc
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = int(x)
        self.y = int(y)
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
