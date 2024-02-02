import pygame


class Grid:
    def __init__(self, screen, start_pos = (100, 100), cell_size=10, width=100, height=50, draw_only_outlines=False) -> None:
        self._screen = screen
        self._start_pos = start_pos
        self._cell_size = cell_size
        self._width = width
        self._height = height

        self._grid_values = [[False]*width for _ in range(height)]

        self._grid_color = (255, 255, 255)
        self._grid_width = 1

        self.draw_only_outlines = draw_only_outlines


    def draw(self) -> None:
        if not self.draw_only_outlines:
            self._draw_inside()

        self._draw_outlines()


    def _draw_inside(self):
        for i in range(1, self._height):
            pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0], self._start_pos[1] + (i*self._cell_size)),
                             (self._start_pos[0] + (self._cell_size*self._width), self._start_pos[1] + (i*self._cell_size)),
                             self._grid_width)

        for i in range(1, self._width):
            pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0] + (i*self._cell_size), self._start_pos[1]),
                             (self._start_pos[0] + i*self._cell_size, self._start_pos[1] + (self._height*self._cell_size)),
                             self._grid_width)


    def _draw_outlines(self):
        # top line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0], self._start_pos[1]),
                             (self._start_pos[0] + (self._cell_size*self._width), self._start_pos[1]),
                             self._grid_width)

        # bottom line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0], self._start_pos[1] + (self._height*self._cell_size)),
                             (self._start_pos[0] + (self._cell_size*self._width), self._start_pos[1] + (self._height*self._cell_size)),
                             self._grid_width)

        # left line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0], self._start_pos[1]),
                             (self._start_pos[0], self._start_pos[1] + (self._height*self._cell_size)),
                             self._grid_width)

        # right line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._start_pos[0] + (self._width*self._cell_size), self._start_pos[1]),
                             (self._start_pos[0] + self._width*self._cell_size, self._start_pos[1] + (self._height*self._cell_size)),
                             self._grid_width)
