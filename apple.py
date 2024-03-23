import random
import pygame as pg
from player import Player

red = (255, 0, 0)
dis_width = 800
dis_height = 800
snake_block = 20

class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(self.screen)

    def spawn(self):
        if pg.Rect.colliderect(self.apple, self.player) is  True:
            self.spawn_x = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0 
            self.spawn_y = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0 

    def draw(self):
        self.apple = pg.draw.rect(self.screen, red, [self.spawn_x, self.spawn_y, 20, 20])

    def update(self):
        pg.self.spawn