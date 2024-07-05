import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define as dimensões da tela e as cores
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Define as posições iniciais da cobra
player_pos1 = [300, 200]
player_pos2 = [280, 200]
player_pos3 = [260, 200]
player = [player_pos1, player_pos2, player_pos3]

# Define a direção inicial da cobra
direction = None

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = 'UP'
    if keys[pygame.K_s]:
        direction = 'DOWN'
    if keys[pygame.K_a]:
        direction = 'LEFT'
    if keys[pygame.K_d]:
        direction = 'RIGHT'

    # Atualiza as posições do corpo da cobra
    if direction:
        for i in range(len(player) - 1, 0, -1):
            player[i] = list(player[i - 1])
        
        # Move a cabeça da cobra
        if direction == 'UP':
            player[0][1] -= 20
        if direction == 'DOWN':
            player[0][1] += 20
        if direction == 'LEFT':
            player[0][0] -= 20
        if direction == 'RIGHT':
            player[0][0] += 20

    # Preenche a tela com a cor preta
    screen.fill(black)

    # Desenha a cobra
    for pos in player:
        pygame.draw.circle(screen, green, pos, 10)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade da cobra
    pygame.time.delay(100)

# Encerra o pygame
pygame.quit()
sys.exit()
