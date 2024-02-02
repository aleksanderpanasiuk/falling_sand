import pygame


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720;
    FPS = 60
    BACKGROUND_COLOR = (23, 23, 23)

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()


    def run(self) -> None:
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            pygame.draw.line(self.screen, (255, 255, 255), (100, 100), (200, 200))

            pygame.display.flip()
            self.screen.fill(self.BACKGROUND_COLOR)
            self.clock.tick(self.FPS)

        pygame.quit()
