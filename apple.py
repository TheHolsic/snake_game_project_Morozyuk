import random
import pygame as pg

red = (255, 0, 0)


class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 600)
    def draw(self):
        pg.draw.rect(self.screen, red, [self.x, self.y, 10, 10])

    def spawn(self):
        pass

    def update(self):
        pass