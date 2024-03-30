import pygame as pg

black = (0, 0, 0)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        self.side = 'RIGHT'
        self.rect = None
        
    def draw(self):
        self.rect = pg.draw.rect(self.screen, black, [self.x, self.y, 20, 20])

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
                self.x += 20
            case 'LEFT':
                self.x -= 20
            case 'UP':
                self.y -= 20
            case 'DOWN':
                self.y += 20

    def update(self):
        pass