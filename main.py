import pygame


def main():
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720;

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 100, 100))

        pygame.display.flip()
        screen.fill((13, 13, 13))
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
