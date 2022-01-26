from pickle import TRUE
import pygame   
from random import *
from math import *

pygame.init()

screen= pygame.display.set_mode((800,600))

pygame.display.set_caption("SPACE INVADER")
icon=pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

#pygame.mixer.music.load("arambh.wav")
#pygame.mixer.music.play(-1)

p1=pygame.image.load("rocket.png")
p1x=400
p1y=500
def player1(p1,x,y):
    screen.blit(p1,(x,y))
change=0


enemy_img=[]
enemy_x=[]
enemy_y=[]
enemy_change_x=[]
enemy_change_y=[]
num_of_enemies=80

y_apply=-200
for i in range(num_of_enemies):
    
    enemy_img.append(pygame.image.load("ufo.png"))
    enemy_x.append(randint(10,600))
    if i!=0:
        enemy_y.append(y_apply)
        y_apply -= randint(100,200)
    else:
        enemy_y.append(50)
    enemy_change_x.append(randint(-2,2))
    enemy_change_y.append(uniform(0.9,0.8))

def enemy1(e1,x,y):
        screen.blit(e1,(x,y))


background_image=pygame.image.load("background.jpg")


fire= pygame.image.load("missile.png")
bullet_state="ready"
bx=0
by=500
def fire_bullet(loc,x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(loc,(x+16,y+10))
bchangey=-10

def explosion(img,x,y):
    screen.blit(img,(x,y))

explosionimg=pygame.image.load("explosion.png")
explosionx=0
explosiony=0
def is_collision(enemyx,enemyy,bulx,buly):
    dist=sqrt((pow((enemyx-bulx),2))+(pow((enemyy-buly),2)))
    if dist<20:
        return True
    else:
        return False


gamewon_img=pygame.image.load("winner.png")

def game_over(x,x1):
    if x == x1:
        return True
    else:
        return False

score=0

font= pygame.font.SysFont("cambria",23)
def score_show(score,x,y):
    score=font.render(str(f"KILLS- {score}"),True,(220,220,220))
    screen.blit(score,(x,y))

font1 =pygame.font.SysFont("cambria",70)

def how_to_play(x,y):
    show=font1.render("SPACE INVADERS",True,(173,216,240))
    screen.blit(show,(x,y))

font2=pygame.font.SysFont("cambria",32)
font3=pygame.font.SysFont("cambria",40)
font4=pygame.font.SysFont("cambria",24)
font5=pygame.font.SysFont("cambria",18)

def continue_game():
    game=font4.render("PRESS Y TO CONTINUE",True,(220,220,220))
    screen.blit(game,(280,410))


def how_to_play1():
    show=font2.render("you are being invaded by aliens",True,(220,220,220))
    show1=font2.render("your task is too finish off the alienships ",True,(220,220,220))
    show2=font2.render("you have 3 chances,3 misses and game over",True,(220,220,220))
    show3=font2.render("if you successfully stop 6 ships from crossing the line",True,(220,220,220))
    show4=font2.render("you win :)",True,(220,220,220))
    show5=font3.render("CONTROLS",True,(173,216,240))
    show6=font4.render("press 'space bar' to shoot",True,(220,220,220))
    show7=font4.render("press 'right arrow' to move right and 'left arrow' to move left",True,(220,220,220))
    show8=font5.render("press space bar to start",True,(220,220,220))
    screen.blit(show,(180,140))
    screen.blit(show1,(140,180))
    screen.blit(show2,(110,220))
    screen.blit(show3,(40,260))
    screen.blit(show4,(300,300))
    screen.blit(show5,(300,400))
    screen.blit(show6,(100,460))
    screen.blit(show7,(100,500))
    screen.blit(show8,(600,560))


scoreboard=pygame.image.load("scoreboard.png")
minus=pygame.image.load("minus.png")

miss=0
def miss_show(miss,x,y):
    miss=font.render(f"MISS - {miss}",True,(220,220,220))
    screen.blit(miss,(x,y))


warning=pygame.image.load("warning.png")

gameover_img=pygame.image.load("gameover.png")

tempcount=0
tempcond=False

running= True

miss_count=300
miss_x=0
miss_y=0

space2_count=0
space_count=0
while running:  
    
    tempcount+=1
    miss_count+=1

    screen.blit(background_image,(0,0))

    if space_count==0:
        space_count1=0    
        while space_count1<1000:
            for events in pygame.event.get():
        
                if events.type == pygame.QUIT:
                    running = False
                    space_count1=1001
                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        
                        space_count1=1001
            
            
            how_to_play(150,30)
            how_to_play1()
            pygame.display.update()
        space_count=2000
    
    
   
    screen.blit(scoreboard,(10,10))
    
    
    screen.blit(minus,(-10,400))
    screen.blit(minus,(114,400))
    screen.blit(minus,(218,400))
    screen.blit(minus,(322,400))
    screen.blit(minus,(426,400))
    screen.blit(minus,(532,400))
    screen.blit(minus,(636,400))
    screen.blit(minus,(740,400))
    screen.blit(minus,(844,400))
    
    
    score_show(score,23,55)
    miss_show(miss,23,83)
  
    
    for events in pygame.event.get():
        
        if events.type == pygame.QUIT:
            running = False

        if events.type==pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                change= -1.5
            if events.key == pygame.K_RIGHT:
                change = 1.5
            if events.key == pygame.K_y:
                miss=0
                score=0

            if events.key == pygame.K_SPACE:               
                if bullet_state=="ready":
                    gun_sound=pygame.mixer.Sound("laser.wav")
                    #gun_sound.play()
                    bx=p1x
                    fire_bullet(fire,bx,by)
    
        if events.type==pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
                change= 0

    p1x += change
    
    

    if p1x <= 0:
        p1x = 0
    elif p1x >= 736:
        p1x = 736

    if bullet_state=="fire":
        by-=3
        fire_bullet(fire,bx,by)

    if by<=0:
        by=500
        bullet_state="ready"

    
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_change_x[i]
        enemy_y[i] += enemy_change_y[i]
           
        
        if enemy_x[i] <= 10:
            enemy_change_x[i] = uniform(-1,1)

        elif enemy_x[i] >= 720:
            enemy_change_x[i] = uniform(-1,1)

        collision = is_collision(enemy_x[i],enemy_y[i],bx,by)
        
        if collision:
            exploded=pygame.mixer.Sound("exploded.wav")
            #exploded.play()
            by=500
            bullet_state="ready"
            score+=1
            tempcond=True
            tempcount=0
            explosiony = enemy_y[i]
            explosionx= enemy_x[i]
            enemy_y[i] =1000

        gamevar=game_over(int(enemy_y[i]),430)
       
        if gamevar:
            miss+=1
            miss_x=enemy_x[i]
            miss_y=enemy_y[i]
            enemy_y[i]=1000
            miss_count=0
        
        if tempcond and tempcount<140:
            explosion(explosionimg,explosionx,explosiony)
        
        if miss_count<50:
            screen.blit(warning,(miss_x,miss_y+15))


        enemy1(enemy_img[i], enemy_x[i], enemy_y[i])
    

   
    player1(p1,p1x,p1y)

    if miss>2 or score>=6:
        for j in range(num_of_enemies):
            enemy_y[j]=1000
        
    if miss>2:
        screen.blit(gameover_img,(140,-40))
        continue_game()
    
    elif score>=6:
        screen.blit(gamewon_img,(280,140))
        continue_game()
    
    
    
    pygame.display.update()


