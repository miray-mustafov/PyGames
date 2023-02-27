import random
import time
import pygame as py
class Retard:
    def __init__(self, papagal):
        self.papagal = papagal

    def get_papagal(self, info):
        return f"{info} etremo {self.papagal}"

py.init()
width, height = 400, 400
game_screen = py.display.set_mode((width, height))
py.display.set_caption("Snake Game")

# Snake position and size
x, y, w, h = 200, 200, 10, 10
delta_x, delta_y = 0, 0
snake_speed = 10
clock = py.time.Clock()
food_x, food_y = random.randint(
    0, width)//10*10, random.randint(0, height)//10*10
body_list = [(x, y)]
game_OVER = False
font = py.font.SysFont('bahnschrift', bold=True, size=25)
grid = [py.Rect(i * w, j * w, w, w) for i in range(w * 4) for j in range(h * 4)]


def snake():
    global x, y, food_x, food_y, game_OVER, snake_speed
    x = (x + delta_x) % width
    y = (y + delta_y) % height

    if (x, y) in body_list[1:]:  # Game Over check
        game_OVER = True
        return

    body_list.append((x, y))

    if food_x == x and food_y == y:
        while (food_x, food_y) in body_list:
            food_x, food_y = random.randint(
                0, width)//10*10, random.randint(0, height)//10*10
        if len(body_list) % 3 == 0:
            snake_speed +=2
    else:
        del body_list[0]
    
    

    game_screen.fill((0, 0, 0))
    score = font.render('Score: '+ str(len(body_list)), True,(255,255,0))
    game_screen.blit(score, [0,0])
    [py.draw.rect(game_screen, (40, 40, 40), cur_rect, 1) for cur_rect in grid]

    py.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, w, h])
    for (i, j) in body_list:
        py.draw.rect(game_screen, (255, 255, 255), [i, j, w, h])
    py.display.update()


while True:
    if game_OVER == True:
        game_screen.fill((0, 0, 0))
        gover_msg = font.render("GAME OVER!", True, (255, 255, 255))
        game_screen.blit(gover_msg, dest = [width//3, height//3])
        
        game_screen.blit(font.render("Final score: "+str(len(body_list)), True, (255,255,0))
            , dest = [width//3, height//3+30])

        py.display.update()
        time.sleep(3)
        py.quit()
        quit()


    events = py.event.get()
    for ev in events:
        if ev.type == py.QUIT:
            py.quit()
            quit()
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_UP:
                if (delta_y != +10):
                    delta_y = -10
                delta_x = 0
            elif ev.key == py.K_DOWN:
                if (delta_y != -10):
                    delta_y = +10
                delta_x = 0
            elif ev.key == py.K_RIGHT:
                if (delta_x != -10):
                    delta_x = +10
                delta_y = 0
            elif ev.key == py.K_LEFT:
                if (delta_x != +10):
                    delta_x = -10
                delta_y = 0
            else:
                continue
            snake()

    if not events:
        snake()
    clock.tick(snake_speed)
