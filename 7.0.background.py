# Pygame Background
import pygame, os
def main():
    pygame.init()

    BLACK   = (   0,   0,   0)
    WHITE   = ( 255, 255, 255)
    GREEN   = (   0, 255,   0)
    RED     = ( 255,   0,   0)
    BLUE    = (   0,   0, 255)

    size = (720, 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    game_over = False

    # background IMG
    bg = pygame.image.load(os.path.join("img", "background.png")).convert()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Definir la imagen como background
        screen.blit(bg, [0, 0])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__=='__main__':
    main()