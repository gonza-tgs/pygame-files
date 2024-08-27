# Pygame Sprites Keyboard Mouse
import pygame, random, os, time

# -- CONSTANTS (constantes) --

# Screen Size (Tamaño pantalla)
SIZE = (720, 720)
SCREEN_WIDTH, SCREEN_HEIGHT = SIZE[0], SIZE[1]
# Screen
SCREEN = pygame.display.set_mode(SIZE)
# bg (Imagen de fondo)
BACKGROUND_IMG = pygame.image.load(os.path.join("img", "background.png")).convert()
# Reloj
CLOCK = pygame.time.Clock()
# Colores
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)

# -- Configs --

# Title Windows (Título de la ventana)
pygame.display.set_caption("PyGame Demo")
# Mouse Visibility (Ver o no el mouse)
pygame.mouse.set_visible(0)


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
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -10
            self.rect.x = random.randrange(SCREEN_WIDTH)

class Player(pygame.sprite.Sprite):
    # Método constructor de la clase Player
    def __init__(self):
        # Llamamos al método super para heredar los métodos y atributos de la super clase Sprite
        super().__init__()
        self.image = pygame.image.load(os.path.join("img", "player.png")).convert()
        self.image.set_colorkey(BLACK)
        # Definimos el atributo self.rect que guarda la posición del objeto instanciado
        self.rect = self.image.get_rect()
        # Coordendas iniciales
        self.rect.x = (SCREEN_WIDTH // 2) - 45
        self.rect.y = (SCREEN_HEIGHT // 4) * 3
        # Definimos la velocidad a 0 de manera predeterminada o inicial
        self.x_speed = 0
        self.y_speed = 0
    # Método para cambiar la velocidad del player
    def change_speed_x(self, x):
        self.x_speed += x

    def change_speed_y(self, y):
        self.y_speed += y

    # Método para mover player usando el valor de self.speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

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

class Game(object):
    def __init__(self):
        # Variable Game Over para controlar el juego
        self.game_over = False

        # Puntaje o Marcador (Score)
        self.score = 0
        # Set de todos los Sprites
        self.all_sprites_set = pygame.sprite.Group()
        # Set de meteoros
        self.meteor_set = pygame.sprite.Group()
        # Set de lasers
        self.laser_set = pygame.sprite.Group()


        # Instanciar meteoros
        for element in range(25):
            meteor = Meteor()
            meteor.rect.x = random.randrange(SCREEN_WIDTH)
            meteor.rect.y = random.randrange(SCREEN_HEIGHT)
            self.meteor_set.add(meteor)
            self.all_sprites_set.add(meteor)

        # Instanciar player
        self.player = Player()
        self.all_sprites_set.add(self.player)


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    # Para realizar el movimiento llamamos al método change_speed() de player
                    self.player.change_speed_x(-3)
                if event.key == pygame.K_d:
                    self.player.change_speed_x(3)
                if event.key == pygame.K_w:
                    # Para realizar el movimiento llamamos al método change_speed() de player
                    self.player.change_speed_y(-3)
                if event.key == pygame.K_s:
                    self.player.change_speed_y(3)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.change_speed_x(3)
                if event.key == pygame.K_d:
                    self.player.change_speed_x(-3)
                if event.key == pygame.K_w:
                    # Para realizar el movimiento llamamos al método change_speed() de player
                    self.player.change_speed_y(3)
                if event.key == pygame.K_s:
                    self.player.change_speed_y(-3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = self.player.rect.x + 45
                laser.rect.y = self.player.rect.y - 20

                self.all_sprites_set.add(laser)
                self.laser_set.add(laser)
                """
                Si se presiona el botón del mouse buttonconsulta si el valor self.game_over es True.
                Si se cumple, se reinicia el juego usando self.__init__() que hace referencia a game = Game()
                """
                if self.game_over:
                    time.sleep(1)
                    self.__init__()

        return False

    def run_logic(self):
        # Si self.game_over no es True, entonces se ejecuta la lógica del Juego.
        if not self.game_over:

            # Llamamos al método update común para cada objeto creado
            self.all_sprites_set.update()

            ## --- COLISIONES --

            for laser in self.laser_set:
                meteor_hit_list = pygame.sprite.spritecollide(laser, self.meteor_set, True)
                for meteor in meteor_hit_list:
                    self.all_sprites_set.remove(laser)
                    self.laser_set.remove(laser)
                    self.score += 1
                    print(self.score)
                if laser.rect.y < -10:
                    self.all_sprites_set.remove(laser)
                    self.laser_set.remove(laser)

                """Cuando se colisiona un laser con meteorito este es removido del meteor_set, por ello,
                cuando eliminamos todos los meteoros, el meteor_set queda vacío y el juego finaliza.
                """
                if len(self.meteor_set) == 0:
                    self.game_over = True

    def display_frame(self, screen):
        # Aplicar img de fondo
        screen.blit(BACKGROUND_IMG, [0, 0])

        # Dibujar texto en pantalla
        if self.game_over:
            font = pygame.font.SysFont("monospace", 25) # Fuente
            text = font.render("GAME OVER, PRESS FIRE TO CONTINUE", True, WHITE) # Texto
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) # Posicionar el texto
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2) # Posicionar el texto
            SCREEN.blit(text, [center_x, center_y]) # Mostrar texto en pantalla

        # Dibujamos los objetos instanciados
        self.all_sprites_set.draw(screen)
        # Actualizar pantalla
        pygame.display.flip()

def main():
    pygame.init()

    done = False
    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(SCREEN)
        CLOCK.tick(60)

    pygame.quit()

if __name__=='__main__':
    main()