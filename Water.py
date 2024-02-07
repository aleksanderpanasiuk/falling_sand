from cellType import CellType
import random


class Water(CellType):
    def __init__(self, screen, screen_position: list, grid_position: list, size: int):
        super().__init__(screen, screen_position, grid_position, size)

        self._color = (0, 102, 255)
        self._last_random_direction = -1
        self._density = 1

    def simulate(self, grid):
        if self._fall(grid):
            return

        else:
            can_move_right = False
            can_move_left = False

            if self._is_valid_position(grid, [self._grid_position[0]+1, self._grid_position[1]]):
                can_move_right = True
            if self._is_valid_position(grid, [self._grid_position[0]-1, self._grid_position[1]]):
                can_move_left = True

            fall_left = False

            if can_move_left and can_move_right:
                if self._last_random_direction == -1:
                    fall_left = random.choice([True, False])
                    self._last_random_direction = fall_left
                else:
                    fall_left = self._last_random_direction

            elif can_move_left:
                fall_left = True
                self._last_random_direction = -1
            elif can_move_right:
                self._last_random_direction = -1

            elif not can_move_left and not can_move_right:
                return

            if fall_left:
                self._move(grid, [-1, 0])
            else:
                self._move(grid, [1, 0])

