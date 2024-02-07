import pygame

class Button:
    def __init__(self, screen, position, width, height, bg_color, text, text_size, text_color) -> None:
        self._screen = screen
        self._position = position
        self._height = height
        self._width = width
        self._bg_color = bg_color
        self._text = text
        self._text_size = text_size
        self._text_color = text_color


    def draw(self):
        pygame.draw.rect(
            self._screen, self._bg_color,
            pygame.Rect(self._position[0], self._position[1], self._height, self._width)
            )

        font = pygame.font.SysFont("Corbel", self._text_size)
        text = font.render(self._text, True, self._text_color)

        self._screen.blit(text, (self._position[0], self._position[1]))

