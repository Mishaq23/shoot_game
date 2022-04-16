from pygame import * 
from random import *


class Game_Sprite(sprite.Sprite):
    def __init__(self, img_name, x, y, w, h, speed):
        super().__init__()
        self.pic = transform.scale(image.load(img_name), (w,h))
        self.rect = self.pic.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = speed

    def reset(self):
        wind.blit(self.pic, (self.rect.x, self.rect.y))
    
class Player(Game_Sprite):
    def update1(self):
        keys = key.get_pressed()
        if (keys[K_LEFT] or keys[K_a]) and self.rect.x >= 10:
            self.rect.x -= self.speed
        elif (keys[K_RIGHT]or keys[K_d]) and self.rect.x <= 590:
            self.rect.x += self.speed
        elif (keys[K_UP]or keys[K_w]) and self.rect.y >= 10:
            self.rect.y -= self.speed
        elif (keys[K_DOWN]or keys[K_s]) and self.rect.y <= 390:
            self.rect.y += self.speed
    
    def shoot(self):
        bullet = Bullet('bul1.jpg', self.rect.x, self.rect.y, 20, 20, 5)
        bul_list.append(bullet)

class Enemy(Game_Sprite):
    def update1(self):
        self.rect.y += self.speed
        if self.rect.x > 25 and self.rect.x < 650:
            self.rect.x += randint(-5, 5)
        else:
            if self.rect.x <= 25:
                self.rect.x += randint(1, 5)
            else:
                self.rect.x += randint(-5, -1)  
        if self.rect.y >= win_h:
            self.rect.y = -30

class Bullet(Game_Sprite):

    def update(self):
        self.rect.y -= self.speed

win_h = 500
win_w = 700
FPS = 60
image_pic = 'space.jpg'

wind = display.set_mode((win_w, win_h))
display.set_caption("Putin's game")
timer = time.Clock()
background = transform.scale(image.load(image_pic), (win_w, win_h))

mixer.init()
mixer.music.load('astral_step.mp3')
mixer.music.play()

putin = Player('putin.jpg', win_h/2, win_h-80, 120, 120, 5)

list_enem = list()
bul_list = list()

for i in range(5):
    enem1 = Enemy('zelen.jpg', randint(20, win_w-20), randint(20, win_h/2), 50, 50, uniform(1, 3))
    list_enem.append(enem1)

game = True 
finish = False

while game:

    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                putin.shoot()
    
    if not finish:
        wind.blit(background, (0, 0))
        putin.reset()
        putin.update1()
        for i in list_enem:
            i.update1()
            i.reset()
        for j in bul_list:
            j.update()
            j.reset()
        display.update()
    timer.tick(FPS)
