import pygame
import random
import cellType


class Grid:
    def __init__(self, screen=None, position = (100, 100), cell_size=10, width=100, height=50, draw_only_outlines=False) -> None:
        self._screen = screen
        self._position = position


        if cell_size <= 0:
            raise TypeError("cell_size must be greater than 0")
        self._cell_size = cell_size

        if width <= 0:
            raise TypeError("width must be greater than 0")
        self._width = width

        if height <= 0:
            raise TypeError("height must be greater than 0")
        self._height = height


        self._grid_values = [[False]*width for _ in range(height)]

        self._grid_color = (100, 100, 100)
        self._grid_width = 1

        self.draw_only_outlines = draw_only_outlines

        self._cell_color = (255, 255, 102)
        self._max_stack = 1

    def events(self, event: pygame.event) -> None:
        if pygame.mouse.get_pressed()[0]:
            self._spawn_sand(pygame.mouse.get_pos())


    def _spawn_sand(self, mouse_pos: tuple) -> None:
        if not self._is_mouse_on_grid(mouse_pos):
            return

        mouse_position_on_grid = self._calculate_mouse_position_on_grid(mouse_pos)

        self._grid_values[mouse_position_on_grid[1]][mouse_position_on_grid[0]] = True


    def _is_mouse_on_grid(self, mouse_pos: tuple) -> bool:
        return self._position[0] <= mouse_pos[0] < self._position[0] + (self._width*self._cell_size) and \
            self._position[1] <= mouse_pos[1] < self._position[1] + (self._height*self._cell_size)


    def _calculate_mouse_position_on_grid(self, mouse_pos: tuple) -> tuple:
        mouse_position_on_grid = (mouse_pos[0]-self._position[0])//self._cell_size, \
                                (mouse_pos[1]-self._position[1])//self._cell_size

        return mouse_position_on_grid


    def simulate(self) -> None:
        for i in range(self._height-2, -1, -1):
            for j in range(self._width):
                if self._grid_values[i][j]:
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


    def draw(self) -> None:
        if self._screen is None:
            return

        if not self.draw_only_outlines:
            self._draw_inside()

        self._draw_outlines()
        self._draw_cells()


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


    def _draw_cells(self) -> None:
        for i, line in enumerate(self._grid_values):
            for j, cell in enumerate(line):
                if cell:
                    pygame.draw.rect(self._screen, self._cell_color,
                        pygame.Rect(
                            self._position[0] + j*self._cell_size, self._position[1] + i*self._cell_size,
                            self._cell_size, self._cell_size
                        )
                    )

