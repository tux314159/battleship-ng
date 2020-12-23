import copy as copy
import pygame as pg
from typing import List
from common_types import Size2d, Coord, Color


class Ship:
    """
    A ship.
    Lol
    """

    HOR = 0
    VER = 1

    def __init__(self, size: Size2d, cell_size: Size2d, colour: Color) -> None:
        self.size = size
        self.colour = colour
        self.cell_size = cell_size

        self.surf: pg.Surface = pg.Surface(
            (self.size.w * self.cell_size.w, self.size.h * self.cell_size.h)
        )
        self.hitmap: List[List[bool]] = [
            [False for _ in range(self.cell_size.w)] for _ in range(self.cell_size.h)
        ]

    def hit_tile(self, cell_coord: Coord) -> None:
        self.hitmap[cell_coord.row][cell_coord.col] = True

    def is_tile_hit_p(self, cell_coord: Coord) -> bool:
        return self.hitmap[cell_coord.row][cell_coord.col]

    def is_ship_sunk_p(self) -> bool:
        ret: bool = True
        for i in range(self.cell_size.h):
            for j in range(self.cell_size.w):
                ret &= self.hitmap[i][j]

        return ret

    def draw(self) -> None:
        pg.draw.rect(
            self.surf,
            self.colour,
            (
                (0, 0),
                (self.size.w * self.cell_size.w, self.size.h * self.cell_size.h),
            ),
        )

    def get_surface(self) -> pg.Surface:
        return copy.copy(self.surf)
