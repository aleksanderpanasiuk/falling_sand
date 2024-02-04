import pygame


class CellType:
    def __init__(self, screen, screen_position: tuple, grid_position: tuple, size: int):
        self._screen = screen
        self._screen_position = screen_position
        self._grid_position = grid_position
        self._size = size

        self._color = (255, 255, 255)

        return self


    def events(self) -> None:
        pass


    def draw(self) -> None:
        pygame.draw.rect(
            self._screen, self._color,
            pygame.Rect(
                self._screen_position[0], self._screen_position[0],
                self._size, self._size
            )
        )
