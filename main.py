import pygame
import random

pygame.mixer.init()

pygame.init()
# print(a)

screen_width = 1500
screen_height = 800

gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SnakeGame")

logo = pygame.image.load("logo1.jpeg")

pygame.display.set_icon(logo)

backimg = pygame.image.load("backimg1.jpg")
backimg = pygame.transform.scale(backimg,(screen_width,screen_height)).convert_alpha()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
yellow = (255,223,0)

# highscore = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,40)

def display_text(text,color,x,y,s):
    screen_text = pygame.font.SysFont(None,s).render(text,True,color)

    gameDisplay.blit(screen_text,[x,y])

def plot_snake(gameDisplay,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameDisplay,color,[x,y,snake_size,snake_size])

def welcome():

    Exit_Game = False

    gameDisplay.fill(black)
    display_text("Welcome To SnakeGame", green , 520,350,50)
    display_text("Press Enter For Start Game...", white , 550,400,35)

    while not Exit_Game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit_Game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("back.mp3.mp3")
                    pygame.mixer.music.play(-1)
                    game_loop()

        pygame.display.update()
        # clock.tick(120)

def game_loop():

    Game_Over = False
    Exit_Game = False

    snake_x = 300
    snake_y = 250
    snake_size = 30

    food_x = random.randint(80,1400)
    food_y = random.randint(100,700)
    food_size = 30

    velocity_x = 0
    velocity_y = 0
    init_speed = 1.5

    fps = 120
    score = 0

    with open("highscore.txt","r") as f:
        highscore = f.read()

    snk_list = []
    snk_length = 1

    while not Exit_Game:
        if Game_Over:

            # pygame.mixer.music.load("gameover.mp3")
            # pygame.mixer.music.play()

            with open("highscore.txt","w") as f:
                f.write(highscore)
                
            gameDisplay.fill(black)
            display_text("Game Over!",green,600,330,60)
            display_text("Score : " + str(score),white,30,20,50)
            display_text("Press Enter for continue...",white ,550,390,40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit_Game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("back.mp3.mp3")
                        pygame.mixer.music.play(-1)
                        game_loop()

        else:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit_Game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # print("You have just pressed space key!")
                        velocity_x = init_speed
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_speed
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_speed
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_speed
                        velocity_x = 0

                    # if event.key == pygame.K_SPACE:
                    #     velocity_x = 0
                    #     velocity_y = 0

            if abs(snake_x - food_x)<30 and abs(snake_y - food_y)<30:
                score += 10

                if score > int(highscore):
                    highscore = str(score)

                # print("Score : ", score * 10)
                # snake_size += food_size
                food_x = random.randint(80,1400)
                food_y = random.randint(100,700)
                snk_length+=10

            if score < 50:
                init_speed = 1.5
            elif score < 150:
                init_speed = 2
            elif score < 300:
                init_speed = 2.5
            elif score < 500:
                init_speed = 3
            elif score < 800:
                init_speed = 3.5
            elif score < 1200:
                init_speed = 4
            elif score < 1500:
                init_speed = 4.5
            else:
                init_speed = 5

            snake_x += velocity_x
            snake_y += velocity_y

            if snake_x <= 0 or snake_x >= screen_width or snake_y <= 0 or snake_y >= screen_height:
                # print("Game Over!")
                # print("Your Score is : ", score)
                Game_Over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play(-1)

            gameDisplay.fill(black)
            gameDisplay.blit(backimg,(0,0))
            # display_text("Score : "+ str(score),white,30,20,50)
            display_text("Score : "+ str(score) +"      Highscore : "+ highscore,white,30,20,50)
            pygame.draw.rect(gameDisplay,red, [food_x,food_y,food_size,food_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                Game_Over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play(-1)

            plot_snake(gameDisplay,green,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()

