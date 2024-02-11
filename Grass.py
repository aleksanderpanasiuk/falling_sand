from cellType import CellType


class Grass(CellType):
    def __init__(self, screen, screen_position: list, grid_position: list, size: int):
        super().__init__(screen, screen_position, grid_position, size)
        self._color = (0, 204, 0)
        self._max_stack = 1

