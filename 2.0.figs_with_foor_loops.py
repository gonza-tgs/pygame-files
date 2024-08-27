# Dibujando figuras con el ciclo FOR
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
color_inventado = (  45, 202, 112)

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
    screen.fill(BLACK)
    
    ### -- ZONA DE DIBUJO
    # For loop nos sirve para crear varias figuras
    # En este caso el range nos servirá con 3 argumentos:
    # (inicio, fin, paso)
    
    # Al ir variando las coordenas podemos cubrir diferentes puntos
    # de la pantalla
    for x in range(0, 800, 50):
        pygame.draw.rect(screen, RED, (x, 50, 50, 50))
    
    for x in range(50, 800, 100):
        pygame.draw.rect(screen, color_inventado, (x, 100, 50, 50))
        
    for x in range(0, 800, 100):
        pygame.draw.rect(screen, tea_green, (x, 150, 50, 50))
    
    for x in range(50, 800, 100):
        pygame.draw.rect(screen, tea_green, (x, 200, 50, 50))
    
    for x in range(0, 800, 100):
        pygame.draw.rect(screen, tea_green, (x, 250, 50, 50))
    
    for x in range(50, 800, 100):
        pygame.draw.rect(screen, tea_green, (x, 300, 50, 50))
        
    for x in range(0, 800, 100):
        pygame.draw.rect(screen, tea_green, (x, 350, 50, 50))
    
    for x in range(50, 800, 100):
        pygame.draw.rect(screen, tea_green, (x, 400, 50, 50))

    # actualizar pantalla
    pygame.display.flip()