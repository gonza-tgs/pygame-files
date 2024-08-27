# Pygame Sprites
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
    # Titulo de la ventana
    pygame.display.set_caption("Sprites")
    pygame.mouse.set_visible(0)
    bg = pygame.image.load(os.path.join("img", "background.png")).convert()
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

    class Player(pygame.sprite.Sprite):
        # Método constructor de la clase Meteor
        def __init__(self):
            # Llamamos al método super para heredar los métodos y atributos de la super clase Sprite
            super().__init__()
            self.image = pygame.image.load(os.path.join("img", "player.png")).convert()
            self.image.set_colorkey(BLACK)
            # Definimos el atributo self.rect que guarda la posición del objeto instanciado
            self.rect = self.image.get_rect()


    pygame.init()
    # Definimos 2 conjuntos o set para guardar los objetos de la clase
    meteor_set = pygame.sprite.Group()
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

        # Mover el player usando el mouse
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]
        """
        Detectar colisiones: Se debe crear lista para guardar las colisiones.
        spritecollide(sprite, grupo de sprites, dokill=True)
        dokill: Define que se hará en la colision:
                - True: para desaparecer el sprite.
                - False: no se hace nada.
        """
        meteor_hit_list = pygame.sprite.spritecollide(player, meteor_set, True)

        # Con un ciclo for aumentamos el puntaje de acuerdo a la cantidad de objetos en lista
        for meteor in meteor_hit_list:
            score += 1
            print(score)

        screen.blit(bg, [0, 0])

        # Dibujamos los objetos instanciados
        all_sprite_set.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__=='__main__':
    main()