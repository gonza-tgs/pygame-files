# Pygame Animations 1
import pygame, sys, random, time

pygame.init()

# definir variables de colores
# Para ello se crear una tuple de 3 números
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)

"""Colores para tu aplicación
Colores en Hex: https://htmlcolorcodes.com/
Paleta de Colores: https://coolors.co/
Para vel codigo RGB
Ir a: Banda superir -> 3 puntos -> settings -> secondary info -> RGB
"""
dark_purple     = (   48,   1,  30)
tea_green       = (  215, 252, 212)

# tamaño de la ventana
size = (1000, 600)

# crear ventana
screen = pygame.display.set_mode(size)

# definir un reloj para manejar los frames per second (FPS) dentro del juego
clock = pygame.time.Clock()

"""
Variables del cuadrado

"""
# definimos unas coordenadas iniciales
x_coord = 400
y_coord = 400

# definimos una velocidad a la que se moverá el cuadrado
x_speed = 50
y_speed = 50

# Tamaño del cuadrado
x_size = 40
y_size = 40

# Ciclo (infinito) de ejecución del juego
while True:
    # ciclo for para recorrer los eventos dentro del juego
    for event in pygame.event.get():
        # Si hacemos click en la X de la ventana salimos del juego
        if event.type == pygame.QUIT:
            sys.exit()

    # --- INICIO LOGICA DEL JUEGO ---

    # Para dar movimiento aumentamos el valor de la coordenada usando el valor de la velocidad
    # Movimiento en X
    x_coord += x_speed
    # Movimiento en Y
    y_coord += y_speed

    """
    Para evitar que el cuadrado salga de la pantalla usamos un condicional.
    Este invierte el signo de la velocidad (multiplicando por -1) usando como referencia
    el valor de la coordanda X en el momento
    Para acceder al valor del tamaño de la pantalla convertimos la tupla "size"
    Luego, accedemos al primer dato de la lista usando su índice [0] o [1],
    A este valor le restamos el tamaño del objeto con x_size
    """
    # Coordenada X
    if (x_coord > (size[0] - x_size) or x_coord < 0):
        x_speed *= -1
    # Coordenada Y
    if (y_coord > (size[1] - y_size) or y_coord < 0):
        y_speed *= -1

    # --- FIN LOGICA DEL JUEGO ---

    # color de fondo
    screen.fill(BLACK)

    # --- INICIO ZONA DE DIBUJO ---

    # Creamos el cuadrado usando las variables declaradas
    pygame.draw.rect(screen, tea_green, (x_coord, y_coord, x_size, y_size))

    # --- FIN ZONA DE DIBUJO ---

    # actualizar pantalla
    pygame.display.flip()

    # tiempo de reloj: cambiando este valor podemos variar los FPS.
    clock.tick(30)