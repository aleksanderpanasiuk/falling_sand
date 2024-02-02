import pygame


class Grid:
    def __init__(self, screen, position = (100, 100), cell_size=10, width=100, height=50, draw_only_outlines=False) -> None:
        self._screen = screen
        self._position = position
        self._cell_size = cell_size
        self._width = width
        self._height = height

        self._grid_values = [[False]*width for _ in range(height)]

        self._grid_color = (255, 255, 255)
        self._grid_width = 1

        self.draw_only_outlines = draw_only_outlines


    def events(self, event: pygame.event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                self._spawn_sand(pygame.mouse.get_pos())


    def _spawn_sand(self, mouse_pos: tuple) -> None:
        if not self._is_mouse_on_grid(mouse_pos):
            return

        mouse_position_on_grid = self._calculate_mouse_position_on_grid(mouse_pos)

        print(mouse_position_on_grid)


    def _is_mouse_on_grid(self, mouse_pos: tuple) -> bool:
        return self._position[0] <= mouse_pos[0] <= self._position[0] + (self._width*self._cell_size) and \
            self._position[1] <= mouse_pos[1] <= self._position[1] + (self._height*self._cell_size)


    def _calculate_mouse_position_on_grid(self, mouse_pos: tuple) -> tuple:
        mouse_position_on_grid = (mouse_pos[0]-self._position[0])//self._cell_size, \
                                (mouse_pos[1]-self._position[1])//self._cell_size

        return mouse_position_on_grid


    def draw(self) -> None:
        if not self.draw_only_outlines:
            self._draw_inside()

        self._draw_outlines()


    def _draw_inside(self) -> None:
        for i in range(1, self._height):
            pygame.draw.line(self._screen, self._grid_color,
                             (self._position[0], self._position[1] + (i*self._cell_size)),
                             (self._position[0] + (self._cell_size*self._width), self._position[1] + (i*self._cell_size)),
                             self._grid_width)

        for i in range(1, self._width):
            pygame.draw.line(self._screen, self._grid_color,
                             (self._position[0] + (i*self._cell_size), self._position[1]),
                             (self._position[0] + i*self._cell_size, self._position[1] + (self._height*self._cell_size)),
                             self._grid_width)


    def _draw_outlines(self) -> None:
        # top line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._position[0], self._position[1]),
                             (self._position[0] + (self._cell_size*self._width), self._position[1]),
                             self._grid_width)

        # bottom line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._position[0], self._position[1] + (self._height*self._cell_size)),
                             (self._position[0] + (self._cell_size*self._width), self._position[1] + (self._height*self._cell_size)),
                             self._grid_width)

        # left line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._position[0], self._position[1]),
                             (self._position[0], self._position[1] + (self._height*self._cell_size)),
                             self._grid_width)

        # right line
        pygame.draw.line(self._screen, self._grid_color,
                             (self._position[0] + (self._width*self._cell_size), self._position[1]),
                             (self._position[0] + self._width*self._cell_size, self._position[1] + (self._height*self._cell_size)),
                             self._grid_width)
