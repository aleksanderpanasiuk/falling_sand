from cellType import CellType


class Sand(CellType):
    def __init__(self, screen, screen_position: tuple, grid_position: tuple, size: int):
        super().__init__(screen, screen_position, grid_position, size)
        self._color = (255, 255, 102)

'''
    def simulate(self, grid):
        if not self._grid_values[i+1][j]:
            self._grid_values[i][j] = False
            self._grid_values[i+1][j] = True

        elif i+self._max_stack < self._height:
            can_fall_left = j > 0
            can_fall_right = j+1 < self._width


            for k in range(1, self._max_stack+1):
                if j > 0 and self._grid_values[i+k][j-1]:
                    can_fall_left = False
                if j+1 < self._width and self._grid_values[i+k][j+1]:
                    can_fall_right = False


            fall_left = False

            if can_fall_left and can_fall_right:
                fall_left = random.choice([True, False])
            elif can_fall_left:
                fall_left = True
            elif not can_fall_left and not can_fall_right:
                continue

            if fall_left:
                self._grid_values[i][j] = False
                self._grid_values[i+1][j-1] = True
            else:
                self._grid_values[i][j] = False
                self._grid_values[i+1][j+1] = True

                '''