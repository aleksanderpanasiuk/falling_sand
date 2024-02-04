from cellType import CellType
import random


class Sand(CellType):
    def __init__(self, screen, screen_position: list, grid_position: list, size: int):
        super().__init__(screen, screen_position, grid_position, size)
        self._color = (255, 255, 102)


    def simulate(self, grid):
        height = len(grid)
        width = len(grid[0])

        if not grid[self._grid_position[1]+1][self._grid_position[0]]:
            grid[self._grid_position[1]][self._grid_position[0]] = None
            grid[self._grid_position[1]+1][self._grid_position[0]] = self
            self._grid_position[1] += 1
            self._screen_position[1] += self._size


        elif self._grid_position[1]+self._max_stack < height:
            can_fall_left = self._grid_position[0] > 0
            can_fall_right = self._grid_position[0]+1 < width


            for k in range(1, self._max_stack+1):
                if self._grid_position[0] > 0 and grid[self._grid_position[1]+k][self._grid_position[0]-1]:
                    can_fall_left = False
                if self._grid_position[0]+1 < width and grid[self._grid_position[1]+k][self._grid_position[0]+1]:
                    can_fall_right = False


            fall_left = False

            if can_fall_left and can_fall_right:
                fall_left = random.choice([True, False])
            elif can_fall_left:
                fall_left = True
            elif not can_fall_left and not can_fall_right:
                return

            if fall_left:
                grid[self._grid_position[1]][self._grid_position[0]] = None
                grid[self._grid_position[1]+1][self._grid_position[0]-1] = self
                self._grid_position[1] += 1
                self._grid_position[0] -= 1
                self._screen_position[1] += self._size
                self._screen_position[0] -= self._size
            else:
                grid[self._grid_position[1]][self._grid_position[0]] = None
                grid[self._grid_position[1]+1][self._grid_position[0]+1] = self
                self._grid_position[1] += 1
                self._grid_position[0] += 1
                self._screen_position[1] += self._size
                self._screen_position[0] += self._size
