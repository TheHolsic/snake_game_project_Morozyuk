import random
import pygame as pg

red = (255, 0, 0)


class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.x = 300
        self.y = 300
    def draw(self):
        pg.draw.rect(self.screen, red, [self.x, self.y, 10, 10])

    def spawn(self):
        pass

    def update(self):
        pass