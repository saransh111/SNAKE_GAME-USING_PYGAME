from random import randint
import pygame

x = pygame.init()
pygame.font.init()
MYfont = pygame.font.SysFont('Comic Sans MS', 48)
abc = pygame.display.set_mode((1200, 659))
pygame.display.set_caption('SNAKE IT UP')

image = pygame.image.load(r'C:\Users\Saransh Bhaduka\PycharmProjects\game_practice\Webp.net-resizeimage.jpg')
img = pygame.image.load(r'C:\Users\Saransh Bhaduka\PycharmProjects\game_practice\Webp.net-resizeimage.png')
def create_snake(
    gamewindow,
    color,
    snk_list,
    snk_size,
    ):
    for (x, y) in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snk_size, snk_size])


def text_screen(
    text,
    color,
    x,
    y,
    ):
    screen_text = MYfont.render(text, True, color)
    abc.blit(screen_text, [x, y])
clock = pygame.time.Clock()
def anotherone():
    exit_game=False
    level=1
    while not exit_game:
        abc.blit(image, (0, 0))
        text_screen("SELECT THE LEVEL YOU WANT TO PLAY AT ", (255,255,0), 50, 200)
        text_screen("LEVEL : " +str(level), (255, 255, 0), 500, 300)
        text_screen("PRESS ENTER TO CONTINUE!!! ", (255, 255, 0), 200, 450)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level=level + 1
                if event.key == pygame.K_DOWN:
                    level = level - 1
                if event.key == pygame.K_RETURN:
                    gameloop(level)
            if level>10:
                level=level-1
            if level<0:
                level=level+1
        pygame.display.update()
        clock.tick(60)
def welcome():
    exit_game = False
    while not exit_game:
        abc.blit(img, (0, 0))
        text_screen("Press Space Bar To Play", (255,255,255), 200, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    anotherone()

        pygame.display.update()
        clock.tick(60)

def gameloop(a):
    exit_game = False
    value1 = randint(0, 1200)
    value2 = randint(0, 500)
    velocity_x = 0
    velocity_y = a
    snake_x = 600
    snake_y = 250
    snake_size = 10
    snake_sizey = 10
    score = 0
    snk_list = []
    snk_size = 5
    game_over = False
    with open("high_score.txt", "r") as f:
        high_score = f.read()
    while not exit_game:
        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            abc.blit(image, (0, 0))
            text_screen('Game Over! Press Enter To Continue', (255, 0,
                        0), 200, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        anotherone()
        else:
            for event in pygame.event.get():
                print (event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = a
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -1*a

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = a

                    if event.key == pygame.K_LEFT:
                        velocity_x = -1*a
                        velocity_y = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            abc.blit(image, (0, 0))
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if head in snk_list[:-1]:
                game_over = True
            if len(snk_list) >= snk_size:
                del snk_list[0]
            if snake_x == 1200 or snake_x == 0 or snake_y == 0 \
                or snake_y == 700:
                game_over = True
            create_snake(abc, (0, 0, 0), snk_list, 30)
            text_screen("Score: " + str(score) , (255,255,0), 5, 5)
            text_screen("High Score: " + str(high_score), (255, 255, 0), 840, 5)
            pygame.draw.rect(abc, (255, 0, 0), [value1, value2, 30, 30])
            if abs(snake_x - value1) < 30 and abs(snake_y - value2) \
                < 30:
                value1 = randint(0, 1200)
                value2 = randint(0, 500)
                score = score + 10
                snk_size = snk_size + 10
                if score > int(high_score):
                    high_score = score
                #create_snake(abc, (0, 0, 0), snk_list, 30)
        pygame.display.update()
        clock.tick(30)


welcome()
