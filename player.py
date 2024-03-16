import pygame as pg

black = (0, 0, 0)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 300
        self.y = 300
        self.side = 'RIGHT'

    def draw(self):
        pg.draw.rect(self.screen, black, [self.x, self.y, 10, 10])

    def move (self, event):
        if event[pg.K_LEFT]:
            self.side = 'LEFT'
        if event[pg.K_RIGHT]:
            self.side = 'RIGHT'
        if event[pg.K_UP]:
            self.side = 'UP'
        if event[pg.K_DOWN]:
            self.side = 'DOWN'
        
        match self.side:
            case 'RIGHT':
                self.x += 10
            case 'LEFT':
                self.x -= 10
            case 'UP':
                self.y -= 10
            case 'DOWN':
                self.y += 10

    def update(self):
        pass