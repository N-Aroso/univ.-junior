import pygame
from pygame.locals import *
import random


def main():

    pygame.init()
    screen = pygame.display.set_mode((960, 560))
    pygame.display.set_caption('Basic Pygame Program')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 150)
    text = font.render("Snake by Nunos", 1, (0, 178, 0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if botao_iniciar_rect.collidepoint(event.pos):
                    game()

        font = pygame.font.SysFont(None, 100)
        texto = font.render("Iniciar Jogo", True, (200, 0, 0))
        botao_iniciar_rect = texto.get_rect(center=(400, 300))
        screen.blit(texto, botao_iniciar_rect)
        
        pygame.display.flip()



def game():

    
    pygame.init()
    screen = pygame.display.set_mode((960, 560))
    clock = pygame.time.Clock() 
    running = True
    # dt = 0

    player_pos1 = pygame.Vector2(440, 270)
    player_pos2 = pygame.Vector2(400, 270)
    player_pos3 = pygame.Vector2(360, 270)

    x= random.randint(0,900)
    y= random.randint(0,500)

    maçapos = pygame.Vector2(x,y)

    counter = 0
    hehe= 0
    vectorw = pygame.Vector2(0,-40)



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("green")

        pygame.draw.circle(screen, "purple", player_pos1, 20)
        pygame.draw.circle(screen, "purple", player_pos2, 20)
        pygame.draw.circle(screen, "purple", player_pos3, 20)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] :
            
            counter+= 1
            if counter % 20 == 0:
                if hehe== 0:
                    player_pos3.y = player_pos1.y - 40
                    player_pos3.x = player_pos1.x
                    pygame.time.delay(100)
                    hehe = 1
                elif hehe==1:   
                    player_pos2.y = player_pos3.y - 40
                    player_pos2.x = player_pos3.x
                    pygame.time.delay(100)
                    hehe = 2
                elif hehe == 2:
                    player_pos1.y = player_pos2.y - 40
                    player_pos1.x = player_pos2.x
                    pygame.time.delay(100)
                    hehe = 0


        if keys[pygame.K_d] :
            counter+= 1
            if counter % 20 == 0:

                if hehe==0:
                    player_pos3.y = player_pos1.y
                    player_pos3.x = player_pos1.x + 40
                    pygame.time.delay(100)
                    hehe = 1
                elif hehe==1:   
                    player_pos2.y = player_pos3.y
                    player_pos2.x = player_pos3.x + 40
                    pygame.time.delay(100)
                    hehe = 2
                elif hehe == 2:
                    player_pos1.y = player_pos2.y 
                    player_pos1.x = player_pos2.x + 40
                    pygame.time.delay(100)
                    hehe = 0

        if keys[pygame.K_s] :
            counter+= 1
            if counter % 20 == 0:
                if hehe==0:
                    player_pos3.y = player_pos1.y + 40
                    player_pos3.x = player_pos1.x
                    pygame.time.delay(100)
                    hehe = 1
                elif hehe==1:   
                    player_pos2.y = player_pos3.y + 40
                    player_pos2.x = player_pos3.x 
                    pygame.time.delay(100)
                    hehe = 2
                elif hehe == 2:
                    player_pos1.y = player_pos2.y  + 40
                    player_pos1.x = player_pos2.x 
                    pygame.time.delay(100)
                    hehe = 0
    
        if keys[pygame.K_a] : 
            counter+= 1
            if counter % 20 == 0:
                if hehe== 0:
                    player_pos3.y = player_pos1.y
                    player_pos3.x = player_pos1.x -40
                    pygame.time.delay(100)
                    hehe = 1
                elif hehe==1:   
                    player_pos2.y = player_pos3.y 
                    player_pos2.x = player_pos3.x - 40
                    pygame.time.delay(100)
                    hehe = 2
                elif hehe == 2:
                    player_pos1.y = player_pos2.y
                    player_pos1.x = player_pos2.x - 40
                    pygame.time.delay(100)
                    hehe = 0


        # if keys[pygame.K_d] :
        #     counter+= 1
        #     if counter % 20 == 0:

        #         if hehe==0:
        #             player_pos3.y = player_pos1.y
        #             player_pos3.x = player_pos1.x + 40
        #             pygame.time.delay(100)
        #             hehe = 1
        # player= [player_pos1,player_pos2,player_pos3]



        # for i in range(len(player)):

        #     if player[i] == player_pos1:
        #         if keys[pygame.K_s]:
        #             player[0] += vector

        #     elif player[-i-2] != player_pos1:
        #         player[-i-2] = player[i]


        #         elif hehe == 2:
        #             player_pos1.y = player_pos2.y 
        #             player_pos1.x = player_pos2.x + 40
        #             pygame.time.delay(100)
        #             hehe = 0

        # if keys[pygame.K_s] :
        #     counter+= 1
        #     if counter % 20 == 0:
        #         if hehe==0:
        #             player_pos3.y = player_pos1.y + 40
        #             player_pos3.x = player_pos1.x
        #             pygame.time.delay(100)
        #             hehe = 1
        #         elif hehe==1:   
        #             player_pos2.y = player_pos3.y + 40
        #             player_pos2.x = player_pos3.x 
        #             pygame.time.delay(100)
        #             hehe = 2
        #         elif hehe == 2:
        #             player_pos1.y = player_pos2.y  + 40
        #             player_pos1.x = player_pos2.x 
        #             pygame.time.delay(100)
        #             hehe = 0
    
        # if keys[pygame.K_a] :
        #     counter+= 1
        #     if counter % 20 == 0:
        #         if hehe==0:
        #             player_pos3.y = player_pos1.y
        #             player_pos3.x = player_pos1.x - 40
        #             pygame.time.delay(100)
        #             hehe = 1
        #         elif hehe==1:   
        #             player_pos2.y = player_pos3.y 
        #             player_pos2.x 

        #             hehe = 2
        #         elif hehe == 2:
        #             player_pos1.y = player_pos2.y 
        #             player_pos1.x = player_pos2.x - 40
        #             pygame.time.delay(100)
        #             hehe = 0

        #             player_pos2.x = player_pos3.x - 40
        #             pygame.time.delay(100)
        #             hehe = 2
        #         elif hehe == 2:
        #             player_pos1.y = player_pos2.y 
        #             player_pos1.x = player_pos2.x - 40
        #             pygame.time.delay(100)
        #             hehe = 0


            


        # player= [player_pos1,player_pos2,player_pos3]



        # for i in range(len(player)):


        #     if player[-0i] != player_pos1:
        #         player[-i-2] = player[i]
        #     elif player[i] == player_pos1:
        #         if keys[pygame.K_s]:
        #             player[0] += vectorw




        if player_pos1.x < 20 or player_pos1.x > 940 or player_pos1.y < 20 or player_pos1.y > 540:
            running = False
        if player_pos2.x < 20 or player_pos2.x > 940 or player_pos2.y < 20 or player_pos2.y > 540:
            running = False
        if player_pos3.x < 20 or player_pos3.x > 940 or player_pos3.y < 20 or player_pos3.y > 540:
            running = False


        if player_pos1 or player_pos2 or player_pos3 == maçapos:
            x= random.randint(0,900)
            y= random.randint(0,500)









        #if keys[pygame.K_w]:
         #   player_pos1.y -= 100 * dt
        #if keys[pygame.K_s]:
         #   player_pos1.y += 100 * dt
        #if keys[pygame.K_a]:
         #   player_pos1.x -= 100 * dt
        #if keys[pygame.K_d]:
         #   player_pos1.x += 100 * dt

        #player_pos2.x = player_pos1.x - 40
        #player_pos3.x = player_pos2.x - 40

        # a= 0
        #v = v0 + at






        #clock.tick(5)
        pygame.display.flip()


main()

pygame.quit()
