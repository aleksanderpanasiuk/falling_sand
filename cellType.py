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

    def simulate(self, grid):
        height = len(grid)
        width = len(grid[0])

        if not grid[self._grid_position[1]+1][self._grid_position[0]]:
            self._move(grid, [0, 1])

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
                self._move(grid, [-1, 1])
            else:
                self._move(grid, [1, 1])

    def _move(self, grid, direction: list):
        grid[self._grid_position[1]][self._grid_position[0]] = None
        grid[self._grid_position[1]+direction[1]][self._grid_position[0]+direction[0]] = self
        self._grid_position[1] += direction[1]
        self._grid_position[0] += direction[0]
        self._screen_position[1] += self._size * direction[1]
        self._screen_position[0] += self._size * direction[0]
