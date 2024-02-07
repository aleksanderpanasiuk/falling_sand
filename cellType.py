import pygame
import random


class CellType:
    def __init__(self, screen, screen_position: list, grid_position: list, size: int):
        self._screen = screen
        self._screen_position = screen_position
        self._grid_position = grid_position
        self._size = size

        self._color = (255, 255, 255)

        self._max_stack = 1
        self._density = 2


    def events(self) -> None:
        pass


    def draw(self) -> None:
        pygame.draw.rect(
            self._screen, self._color,
            pygame.Rect(
                self._screen_position[0], self._screen_position[1],
                self._size, self._size
            )
        )

    def _fall(self, grid) -> bool:
        if self._is_valid_position(grid, [self._grid_position[0], self._grid_position[1]+1]):
            self._move(grid, [0, 1])
            return True

        return False


    def simulate(self, grid):
        height = len(grid)
        width = len(grid[0])

        if self._fall(grid):
            return

        elif self._grid_position[1]+self._max_stack < height:
            can_fall_left = self._grid_position[0] > 0
            can_fall_right = self._grid_position[0]+1 < width


            for k in range(1, self._max_stack+1):
                if not self._is_valid_position(grid, [self._grid_position[0]-1, self._grid_position[1]+k]):
                    can_fall_left = False
                if not self._is_valid_position(grid, [self._grid_position[0]+1, self._grid_position[1]+k]):
                    can_fall_right = False


            fall_left = False

            if can_fall_left and can_fall_right:
                fall_left = random.choice([True, False])
            elif can_fall_left:
                fall_left = True
            elif not can_fall_left and not can_fall_right:
                return

            if fall_left:
                self._move(grid, [-1, 1])
            else:
                self._move(grid, [1, 1])

    def _move(self, grid, direction: list):
        grid[self._grid_position[1]][self._grid_position[0]], grid[self._grid_position[1]+direction[1]][self._grid_position[0]+direction[0]] = \
        grid[self._grid_position[1]+direction[1]][self._grid_position[0]+direction[0]], grid[self._grid_position[1]][self._grid_position[0]]

        if grid[self._grid_position[1]][self._grid_position[0]]:
            grid[self._grid_position[1]][self._grid_position[0]].change_position([-direction[0], -direction[1]])

        self.change_position(direction)


    @property
    def denstity(self):
        return self._density


    def change_position(self, direction):
        self._grid_position[1] += direction[1]
        self._grid_position[0] += direction[0]
        self._screen_position[1] += self._size * direction[1]
        self._screen_position[0] += self._size * direction[0]


    def _is_valid_position(self, grid, position) -> bool:
        if 0 <= position[1] < len(grid) and 0 <= position[0] < len(grid[0]):
            if not grid[position[1]][position[0]]:
                return True

            return self._density > grid[position[1]][position[0]].denstity

        return False
