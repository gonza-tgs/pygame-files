# Pygame Pong
import pygame, sys
def main():
    pygame.init()

    size = (800, 600)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    game_over = False

    # Colors
    BLACK   = (   0,   0,   0)
    WHITE   = ( 255, 255, 255)
    GREEN   = (   0, 255,   0)
    RED     = ( 255,   0,   0)
    BLUE    = (   0,   0, 255)

    # Players Size
    # ancho
    player_width = 15
    # alto
    player_height = 90

    # Player 1 coordenadas y velocidad
    x_coord_p1 = size[0] - (750 + player_width/2)
    y_coord_p1 = size[1]/2 - player_height/2
    y_speed_p1 = 0

    # Player 2 coordenadas y velocidad
    x_coord_p2 = size[0] - (50 + player_width/2)
    y_coord_p2 = size[1]/2 - player_height/2
    y_speed_p2 = 0

    # Ball
    # radio del círculo
    ball_radius = 10
    # coordenada en x e y
    x_coord_ball = size[0]/2
    y_coord_ball = size[1]/2
    # velocidad en x e y
    x_speed_ball = 3
    y_speed_ball = 3

    # Puntaje
    puntaje = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                # player 1 movement
                if event.key == pygame.K_w:
                    y_speed_p1 = -3
                elif event.key == pygame.K_s:
                    y_speed_p1 = 3

                # player 2 movement
                elif event.key == pygame.K_UP:
                    y_speed_p2 = -3
                elif event.key == pygame.K_DOWN:
                    y_speed_p2 = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_speed_p1 = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed_p2 = 0

        ## --- INICIO ZONA DE LÓGICA ---

        # Movimiento de los Players
        y_coord_p1 += y_speed_p1
        y_coord_p2 += y_speed_p2

        # Evitar que los Player salgan de la pantalla

        if (y_coord_p1 > (size[1] - player_height) or y_coord_p1 < 0):
            y_speed_p1 *= -1

        if (y_coord_p2 > (size[1] - player_height) or y_coord_p2 < 0):
            y_speed_p2 *= -1
        
        # Movimiento de la Ball
        x_coord_ball += x_speed_ball
        y_coord_ball += y_speed_ball
        
        # Evitar que la ball salga de la pantalla
        if (x_coord_ball > (size[0] - ball_radius) or x_coord_ball < 0):
            x_speed_ball *= -1

        if (y_coord_ball > (size[1] - ball_radius) or y_coord_ball < 0):
            y_speed_ball *= -1
        
        ## --- FIN ZONA DE LÓGICA ---

        screen.fill(BLACK)

        # --- INICIO ZONA DE DIBUJO ---

        player1 = pygame.draw.rect(screen, WHITE, (x_coord_p1, y_coord_p1, player_width, player_height))
        player2 = pygame.draw.rect(screen, WHITE, (x_coord_p2, y_coord_p2, player_width, player_height))

        ball = pygame.draw.circle(screen, WHITE, (x_coord_ball, y_coord_ball), ball_radius)

        # --- FIN ZONA DE DIBUJO ---
        
        # Colisiones
        
        if ball.colliderect(player1) or ball.colliderect(player2):
            x_speed_ball *= -1
            puntaje += 100

        font = pygame.font.SysFont("monospace", 25) # Fuente
        text = font.render(f"Puntos: {puntaje}", False, WHITE) # Texto
        center_x = 10 # Posicionar el texto
        center_y = 10 # Posicionar el texto
        screen.blit(text, [center_x, center_y]) # Mostrar texto en pantalla

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
if __name__=='__main__':
    main()