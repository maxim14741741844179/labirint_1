#создай игру "Лабиринт"!
#help
from pygame import *
font.init()
font1 = font.SysFont('Arial', 70)
winwin = font1.render('YOU WIN', True, (24, 14, 25))
winlose = font1.render('YOU LOSE', True, (25, 2, 2))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

win = display.set_mode((700, 500))
display.set_caption('лабиринт')
bg = transform.scale(image.load('images (6).jfif'), (700, 500))
game = True
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if  self.rect.x >= 700 - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, w, h, color, x, y):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

wall1 = Wall(20, 400, (123, 136, 35), 150, 100)
wall2 = Wall(20, 400, (84, 84, 234), 300, 0) 
wall3 = Wall(20, 400, (47, 84, 84), 450, 100) 
wall4 = Wall(150, 30, (2, 41, 142), 550, 250) 
wall5 = Wall(150, 30, (254, 41, 2), 470, 100)         
player = Player('hero.png', 65, 65, 5, 50, 400)
enemy = Enemy('minos_processed.jpg',65, 65, 3, 500, 300)
gold = GameSprite('treasure.png', 70, 70, 0, 500, 400)

walls = sprite.Group()
walls.add(wall1, wall2, wall3, wall4, wall5)

finish = False
game = True

while game:
    if finish != True:
        win.blit(bg, (0, 0))
        player.update()
        enemy.update()
        player.reset()
        enemy.reset()
        gold.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        if len(sprite.spritecollide(player, walls, False)) > 0:
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, gold):
            win.blit(winwin, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(player, enemy):
            win.blit(winlose, (200, 200))
            finish = True
            kick.play()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(60)
    display.update()
