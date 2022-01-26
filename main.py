import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))

pygame.display.set_caption('Nokia Wala Snake')
icon =pygame.image.load("test.jpg")
pygame.display.set_icon(icon)

player_1=pygame.image.load("snake.png")
player1_x=400
player1_y=300

def player1(x,y):
    screen.blit(player_1,(x,y))

running=True
while running:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running=False
        change=0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change = -5
            if event.key == pygame.K_RIGHT:
                change = 5

        player1_x += change
    screen.fill((140,140,140))
    player1(player1_x,player1_y)
    pygame.display.update()