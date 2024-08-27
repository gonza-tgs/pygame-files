# Pygame Animations 2
import pygame, sys, random, time
pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)

dark_purple     = (   48,   1,  30)
tea_green       = (  215, 252, 212)

"""
Para dar una posición inicial aleatoria a los círculos creamos una lista vacía
Luego llenamos esa lista con listas con 2 elementos, que representan las coordenadas X e Y.
Para generar las coordenadas de manera aleatoria usamos randint
Si queremos más círculos aumentamos el valor de range
"""
coord_list = []

for element in range(60):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coord_list.append([x, y])

# velocidad de movimiento
y_speed = -2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)

    # Usando un ciclo for animamos los círculos usando como base la lista creada
    for coord in coord_list:
        # La coordenda X es coord[0] y la Y es coord[1]
        pygame.draw.circle(screen, tea_green, (coord[0], coord[1]), 5)
        # para dar movimiento vertical, aumentamos el valor de la coord Y
        coord[1] += y_speed

        # Para hacer que sea un movimiento continuo
        # reiniciamos el valor de la coord Y a 0 si este sale de la pantalla.
        if (coord[1] < 0):
            coord[1] = size[1]


    pygame.display.flip()
    clock.tick(30)