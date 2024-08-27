# Pygame Mouse
import pygame, sys
def main():
    pygame.init()

    BLACK   = (   0,   0,   0)
    WHITE   = ( 255, 255, 255)
    GREEN   = (   0, 255,   0)
    RED     = ( 255,   0,   0)
    BLUE    = (   0,   0, 255)

    size = (800, 500)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    # Hacer al mouse invisible
    pygame.mouse.set_visible(1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Obtener la posición del mouse
        mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        # Asignar a una variable las coordenadas obtenidas
        x = mouse_pos[0]
        y = mouse_pos[1]

        screen.fill(BLACK)

        # Asignar la posición del mouse a las coordenadas obtenidas
        pygame.draw.rect(screen, RED, (x, y, 50, 50))
        pygame.draw.circle(screen, RED, (x, y), 50)

        pygame.display.flip()
        clock.tick(60)

if __name__=='__main__':
    main()