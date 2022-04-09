from pygame import * 

class Game_Sprite(sprite.Sprite):
    def __init__(self, img_name, x, y, w, h, speed):
        super().__init__()
        self.pic = transform.scale(image.load(img_name), (w,h))
        self.rect = self.pic.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = speed
        self.k = 0

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

win_h = 500
win_w = 700
FPS = 60
image_pic = 'space.jpg'

wind = display.set_mode((win_w, win_h))
timer = time.Clock()
background = transform.scale(image.load(image_pic), (win_w, win_h))
mixer.music.load('astal_step.mp3')
mixer.music.play()

putin = Player('putin.jpg', win_h/2, win_h-80, 120, 120, 5)

game = True 
finish = False

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    if not finish:
        wind.blit(background, (0, 0))
        putin.reset()
        putin.update1()
        display.update()
    timer.tick(FPS)

    