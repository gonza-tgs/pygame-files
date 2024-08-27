# Pygame Keyboard
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
    
    # Tamaño del objeto
    x_size = 50
    y_size = 50
    
    # Coordenadas del Objeto para que comience en la parte central
    x_coord = size[0]/2 - x_size/2
    y_coord = size[1]/2 - y_size/2

    # Velocidad
    x_speed = 0
    y_speed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # -- EVENTOS DE TECLADO (keyboard) --
            """
            Cada evento que ocurre en el juego es representado por event.type
            Con un condicional verificamos a qué evento corresponde
            pygame.KEYDOWN representa a las teclas presionadas
            pygame.KEYUP representa a las teclas liberadas
            Cada tecla presionada o liberada es representa por event.key
            Con un nuevo condicional verificamos de qué tecla se trata, y de acuerdo a esto
            se realiza un acción u otra.
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Disminuimos la velocidad del eje X
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    # Aumentamos la velocidad del eje X
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    # Disminuimos la velocidad del eje Y
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    # Aumentamos la velocidad del eje Y
                    y_speed = 3

            # Lo mismo de arriba pero para las teclas liberadas
            if event.type == pygame.KEYUP:
                # Otra forma de realizar el código usando menos líneas.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        # Para evitar que la figura salga de la pantalla usamos el mismo código de ejemplos anteriores
        # Coordenada Y
        if (x_coord > (size[0] - x_size) or x_coord < 0):
            x_speed *= -1
        # Coordenada Y
        if (y_coord > (size[1] - y_size) or y_coord < 0):
            y_speed *= -1

        screen.fill(BLACK)
        # Aumentamos el valor de la coordenada X o Y según se presionan o liberan las teclas indicadas
        x_coord += x_speed
        y_coord += y_speed

        # Dibujamos el objeto de acuerdo a las coordenadas indicadas
        pygame.draw.rect(screen, RED, (x_coord, y_coord, x_size, y_size))

        pygame.display.flip()
        clock.tick(60)

if __name__=='__main__':
    main()