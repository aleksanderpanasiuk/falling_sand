import pygame
import Grid


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720;
    FPS = 60
    BACKGROUND_COLOR = (23, 23, 23)

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()

        self._grid = Grid.Grid(self._screen)


    def run(self) -> None:
        self._running = True

        while self._running:
            self._events()
            self._simulate()
            self._draw()

            self._clock.tick(self.FPS)

        pygame.quit()


    def _events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._running = False

            self._grid.events(event)


    def _simulate(self) -> None:
        self._grid.simulate()


    def _draw(self) -> None:
        self._screen.fill(self.BACKGROUND_COLOR)

        self._grid.draw()

        pygame.display.flip()

