import pygame
import Grid
from utils import button


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720;
    FPS = 60
    BACKGROUND_COLOR = (23, 23, 23)

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()

        self._grid = Grid.Grid(self._screen)

        self._materials = ["sand", "rock", "water", "grass"]
        self._current_material = 0

        self._sand_button = button.Button(
            self._screen, (self.SCREEN_WIDTH/2 - 130 - 50, 30), 50, 100, (255, 255, 102),
            "Sand: 1", 35, (60, 60, 60)
            )

        self._rock_button = button.Button(
            self._screen, (self.SCREEN_WIDTH/2 - 50, 30), 50, 100, (60, 60, 60),
            "Rock: 2", 35, (200, 200, 200)
            )

        self._water_button = button.Button(
            self._screen, (self.SCREEN_WIDTH/2 + 130 - 50, 30), 50, 100, (0, 102, 255),
            "Water: 3", 35, (200, 200, 200)
            )


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

                if event.key == pygame.K_1:
                    self._current_material = 0
                elif event.key == pygame.K_2:
                    self._current_material = 1
                elif event.key == pygame.K_3:
                    self._current_material = 2
                elif event.key == pygame.K_4:
                    self._current_material = 3


            if pygame.mouse.get_pressed()[0]:
                self._grid.spawn_cell(pygame.mouse.get_pos(), self._materials[self._current_material])

            self._grid.events(event)


    def _simulate(self) -> None:
        self._grid.simulate()


    def _draw(self) -> None:
        self._screen.fill(self.BACKGROUND_COLOR)

        self._grid.draw()

        self._sand_button.draw()
        self._rock_button.draw()
        self._water_button.draw()

        pygame.display.flip()

