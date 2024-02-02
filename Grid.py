import pygame


class Grid:
    def __init__(self, screen, start_pos = (100, 100), cell_size=10, width=100, height=50) -> None:
        self._screen = screen
        self._start_pos = start_pos
        self._cell_size = cell_size
        self._width = width
        self._height = height

        self._grid_values = [[False]*width for _ in range(height)]

        self._grid_color = (255, 255, 255)
        self._grid_width = 1



    def draw(self) -> None:
        for i in range(self._height + 1):
            pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0], self._start_pos[1] + (i*self._cell_size)),
                             (self._start_pos[0] + (self._cell_size*self._width), self._start_pos[1] + (i*self._cell_size)),
                             self._grid_width)

        for i in range(self._width + 1):
            pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0] + (i*self._cell_size), self._start_pos[1]),
                             (self._start_pos[0] + i*self._cell_size, self._start_pos[1] + (self._height*self._cell_size)),
                             self._grid_width)
