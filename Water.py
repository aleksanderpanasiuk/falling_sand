from cellType import CellType
import random


class Water(CellType):
    def __init__(self, screen, screen_position: list, grid_position: list, size: int):
        super().__init__(screen, screen_position, grid_position, size)

        self._color = (0, 102, 255)

    def simulate(self, grid):
        height = len(grid)
        width = len(grid[0])

        if not grid[self._grid_position[1]+1][self._grid_position[0]]:
            self._move(grid, [0, 1])

        else:
            can_move_right = False
            can_move_left = False

            if self._grid_position[0]+1 < width and not grid[self._grid_position[1]][self._grid_position[0]+1]:
                can_move_right = True
            if self._grid_position[0]-1 >= 0 and not grid[self._grid_position[1]][self._grid_position[0]-1]:
                can_move_left = True

            fall_left = False

            if can_move_left and can_move_right:
                fall_left = random.choice([True, False])
            elif can_move_left:
                fall_left = True
            elif not can_move_left and not can_move_right:
                return

            if fall_left:
                self._move(grid, [-1, 0])
            else:
                self._move(grid, [1, 0])

