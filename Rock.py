from cellType import CellType


class Rock(CellType):
    def __init__(self, screen, screen_position: list, grid_position: list, size: int):
        super().__init__(screen, screen_position, grid_position, size)
        self._color = (179, 179, 179)
        self._max_stack = 2

