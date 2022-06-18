from contextlib import redirect_stderr

import pygame
import os
import random
#music
pygame.mixer.init()

pygame.init()



#Colourss
white = (255 ,255 ,255)
red = (255 , 0,0)
black = (0,0,0)

#creating window
screen_width = 500
screen_height= 300
gameWindow = pygame.display.set_mode((screen_width , screen_height))
#Background image
bgimg = pygame.image.load("snake1.png")
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()

# Game Ovr image
ovimg = pygame.image.load("snake.jpg")
ovimg = pygame.transform.scale(ovimg, (screen_width,screen_height)).convert_alpha()

#welcome Image
weimg = pygame.image.load("welcome.jpg")
weimg = pygame.transform.scale(weimg, (screen_width,screen_height)).convert_alpha()


# Game Tital
pygame.display.set_caption("Snake_Game with Misabh")
pygame.display.update()
clock =  pygame.time.Clock()
font = pygame.font.SysFont(None , 55)
def text_screen(text,color,x,y):
    screen_text = font.render(text, True , color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow , color , snake_list ,snake_size):
    
    for x,y in snake_list:
       pygame.draw.rect(gameWindow ,black, [x , y ,snake_size , snake_size])

#welcome screen 
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,209))
        gameWindow.blit(weimg,(0,0))
        # text_screen("Welcome To Snake Game",black,30,100)
        # text_screen("press Space Bar To Play",black,30,140)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #background song
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)

def gameloop():

            #game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 5
    snake_size = 10
    fps = 30
    #check if high score file exist
    
    if(not os.path.exists("highScore.txt")):
        with open("highScore.txt","w") as f:
            f.write("0")
            
    with open("highScore.txt","r") as f:
        highScore =f.read()
        #snake length variable
    snake_list =[]
    snake_length = 1
        #Game Loop
    while not exit_game:
        if game_over:
            with open("highScore.txt","w") as f:
             f.write(str(highScore))
            gameWindow.fill(white)
            #background change
            gameWindow.blit(ovimg,(0,0))
            text_screen('''Game Over! ''', red , 10 , 100)
            text_screen('''Press Enter to Continue ''', red , 10 , 130)
            text_screen("High Score : "+highScore,red,20,160)
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                     exit_game = True


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome()
                        #  gameloop()
                
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                                                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0
                    if event.key == pygame.K_LEFT:
                            velocity_x = -init_velocity
                            velocity_y = 0
                    if event.key == pygame.K_UP:
                            velocity_y = -init_velocity
                            velocity_x = 0
                    if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0
                            #cheating key if i press Q then my score is update
                    if event.key==pygame.K_q:
                        score+=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
                
            if abs(snake_x - food_x)<6 and abs(snake_y- food_y)<6:
                    score +=10
                    # pygame.mixer.music.load('beep.mp3')
                    # pygame.mixer.music.play()
                    food_x = random.randint(20, screen_width/2)
                    food_y = random.randint(20, screen_height/2)
                    snake_length +=3
                    
                    
                    if score>int(highScore):
                        highScore =score


            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("score: "+ str(score) + "  High Score : "+str(highScore), red , 5,5)
            pygame.draw.rect(gameWindow , red , [food_x, food_y ,snake_size , snake_size])
                
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len (snake_list)>snake_length :
                    del snake_list[0]

            if head in snake_list[:-1]:
                    game_over =True
                    pygame.mixer.music.load('gameOver.mp3')
                    pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                    game_over = True
                    
                    pygame.mixer.music.load('gameOver.mp3')
                    pygame.mixer.music.play()
                    
            
            plot_snake(gameWindow , black , snake_list , snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()