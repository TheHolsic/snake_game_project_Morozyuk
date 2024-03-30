import random
import pygame as pg

red = (255, 0, 0)
dis_width = 800
dis_height = 800
snake_block = 20

class Apple:
    def __init__(self, screen, player):
        pg.init()
        self.screen = screen
        self.player = player
        self.spawn_x = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0 
        self.spawn_y = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0 

    def spawn(self):
        if self.apple.colliderect(self.player):
            self.spawn_x = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0 
            self.spawn_y = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0 
            f1 = pg.font.Font(None, 36)
            text1 = f1.render('Hello Привет', 1, (180, 0, 0))
            self.screen.blit(text1, (10, 50))


    def draw(self):
        self.apple = pg.draw.rect(self.screen, red, [self.spawn_x, self.spawn_y, 20, 20])

    def update(self):
        self.spawn()