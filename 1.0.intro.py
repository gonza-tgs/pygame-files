# Pygame Intro
import pygame, sys

pygame.init()

# Darle nombre a la ventana
pygame.display.set_caption("Qué pasaaa oeee")

# definir variables de colores
# Para ello se crear una tuple de 3 números
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)
amarillo = (255, 212, 51)
naranja = (211, 84, 0)
morado = (165, 51, 255)

"""Colores para tu aplicación
Colores en Hex: https://htmlcolorcodes.com/
Paleta de Colores: https://coolors.co/
Para vel codigo RGB
Ir a: Banda superir -> 3 puntos -> settings -> secondary info -> RGB
"""

dark_purple     = (   48,   1,  30)
tea_green       = (  215, 252, 212)

# tamaño de la ventana
size = (800, 500)

# crear ventana
screen = pygame.display.set_mode(size)

# Ciclo (infinito) de ejecución del juego
while True:
    # ciclo for para recorrer los eventos dentro del juego
    for event in pygame.event.get():
        # Si hacemos click en la X salimos del juego
        if event.type == pygame.QUIT:
            sys.exit()
    # color de fondo
    screen.fill(morado)

    # Zona de dibujo

    # -- Dibujar líneas rectas
    # pantalla (screen), color, [coordenadas de inicio: X, Y], [coordenadas de fin: X,Y], ancho (width)
    # pygame.draw.line(screen, GREEN, [0, 0], [300, 300], 5)
    # pygame.draw.line(screen, RED, [0, 300], [300, 300], 3)
    # pygame.draw.line(screen, BLUE, [0, 300], [300, 500], 3)

    # pygame.draw.line(screen, GREEN, [800, 0], [500, 300], 3)
    # pygame.draw.line(screen, RED, [500, 300], [800, 300], 3)
    # pygame.draw.line(screen, BLUE, [800, 300], [500, 500], 3)

    # -- Dibujar cuadrados o rectángulos
    # pantalla (screen), color, (x, y, ancho, alto)
    pygame.draw.rect(screen, dark_purple, (0, 0, 400, 400))

    # -- Dibujar círculos
    # pantalla (screen), color, (x, y), radio)
    pygame.draw.circle(screen, tea_green, (400, 500/2), 100)

    # actualizar pantalla
    pygame.display.flip()