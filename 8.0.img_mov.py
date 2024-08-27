# Pygame Images
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
    pygame.mouse.set_visible(0)

    # background IMG
    bg = pygame.image.load(os.path.join("img", "background.png")).convert()

    # player IMG
    player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
    # remover el color de fondo del player
    player_img.set_colorkey(BLACK)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0]
        y = mouse_pos[1]

        # Imagen de fondo
        screen.blit(bg, [0, 0])

        # Imagen del player
        screen.blit(player_img, [x, y])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__=='__main__':
    main()