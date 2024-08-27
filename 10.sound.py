# Pygame Sounds
"""
Importante:
Solo se puede usar sonidos en formato o extensión ogg o wav
"""

import pygame, random, os
def main():

    BLACK   = (   0,   0,   0)
    WHITE   = ( 255, 255, 255)
    GREEN   = (   0, 255,   0)
    RED     = ( 255,   0,   0)
    BLUE    = (   0,   0, 255)

    size = (720, 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    game_over = False
    pygame.display.set_caption("Sprites")
    pygame.mouse.set_visible(0)
    bg = pygame.image.load(os.path.join("img", "background.png")).convert()
    # Sonidos
    # Iniciamos el módulo mixer de pygame
    pygame.mixer.init()
    # Creamos una variable para guardar el sonido del laser
    laser_sound = pygame.mixer.Sound(os.path.join("sound", "laser5.ogg"))
    
    # Puntaje o Marcador (Score)
    score = 0
    # -- Definición de Clases --

    class Meteor(pygame.sprite.Sprite):
        # Método constructor de la clase Meteor
        def __init__(self):
            # Llamamos al método super para heredar los métodos y atributos de la super clase Sprite
            super().__init__()
            self.image = pygame.image.load(os.path.join("img", "meteor.png")).convert()
            self.image.set_colorkey(BLACK)
            # Definimos el atributo self.rect que guarda la posición del objeto instanciado
            self.rect = self.image.get_rect()
        # Creamos el método update para dar movimiento a los meteoros
        def update(self):
            # Aumentamos la coordenada y de los meteoros
            self.rect.y += 1
            # Si salen de la pantalla vuelven a aparecer de manera random
            if self.rect.y > size[1]:
                self.rect.y = -10
                self.rect.x = random.randrange(size[0])

    class Player(pygame.sprite.Sprite):
        # Método constructor de la clase Player
        def __init__(self):
            # Llamamos al método super para heredar los métodos y atributos de la super clase Sprite
            super().__init__()
            self.image = pygame.image.load(os.path.join("img", "player.png")).convert()
            self.image.set_colorkey(BLACK)
            # Definimos el atributo self.rect que guarda la posición del objeto instanciado
            self.rect = self.image.get_rect()
            # Definimos la velocidad a 0 de manera predeterminada o inicial
            self.x_speed = 0
            self.y_speed = 0

        # Método para cambiar la velocidad del player
        def change_speed(self, x):
            self.x_speed += x

        # Método para mover player usando el valor de self.speed
        def update(self):
            self.rect.x += self.x_speed
            self.rect.y = 510

    class Laser(pygame.sprite.Sprite):
    # Método constructor de la clase Laser
        def __init__(self):
            # Llamamos al método super para heredar los métodos y atributos de la super clase Sprite
            super().__init__()
            self.image = pygame.image.load(os.path.join("img", "laser.png")).convert()
            self.image.set_colorkey(BLACK)
            # Definimos el atributo self.rect que guarda la posición del objeto instanciado
            self.rect = self.image.get_rect()

        # Método para dar movimiento al laser, este mov. es solo en el eje Y
        # Para que sea un mov. asc. se debe restar a la coordenada actual
        def update(self):
            self.rect.y -= 5

    pygame.init()

    # Definimos conjuntos o set para guardar los objetos de la clase
    meteor_set = pygame.sprite.Group()
    laser_set = pygame.sprite.Group()
    all_sprite_set = pygame.sprite.Group()

    # Instanciar 1 objeto de la clase Player
    player = Player()
    # agregar el player al conjunto de sprites
    all_sprite_set.add(player)

    # Con un for comenzamos a crear o instanciar los objetos de la clase Meteor
    for element in range(50):
        meteor = Meteor()
        # Damos coordendas aleatorias a cada objeto creado
        meteor.rect.x = random.randrange(size[0])
        meteor.rect.y = random.randrange(size[1])
        # agregamos el objeto creado al conjunto
        meteor_set.add(meteor)
        all_sprite_set.add(meteor)


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # Configuramos las teclas que usaremos para mover el player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    # Para realizar el movimiento llamamos al método change_speed() de player
                    player.change_speed(-3)
                if event.key == pygame.K_d:
                    player.change_speed(3)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.change_speed(3)
                if event.key == pygame.K_d:
                    player.change_speed(-3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 20
                # Agregamos el sonido para que se reproduzca usando el nombre ed variable y el método play()
                laser_sound.play()

                all_sprite_set.add(laser)
                laser_set.add(laser)

        # Llamamos al método update común para cada objeto creado
        all_sprite_set.update()

        ## --- COLISIONES --

        for laser in laser_set:
            meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_set, True)
            for meteor in meteor_hit_list:
                all_sprite_set.remove(laser)
                laser_set.remove(laser)
                score += 1
                print(score)
            if laser.rect.y < -10:
                all_sprite_set.remove(laser)
                laser_set.remove(laser)

        screen.blit(bg, [0, 0])

        # Dibujamos los objetos instanciados
        all_sprite_set.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__=='__main__':
    main()