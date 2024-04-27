import pygame as pg

black = (0, 0, 0)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        self.side = 'RIGHT'
        self.rect = None
        self.count = 0
        self.last_move = [self.x, self.y]
        self.tail = [self.last_move]
        self.chage_block = 0

    def draw(self):
        self.rect = pg.draw.rect(self.screen, black, [self.x, self.y, 20, 20])
        if len(self.tail) > 1:
            self.draw_tail()

    def draw_tail(self):
        for i in range(len(self.tail)):
            pg.draw.rect(self.screen, black, [self.tail[i][0], self.tail[i][1], 20, 20])

    def chack_game_over(self):
        new_tail = self.tail[1:]
        for i in range(len(new_tail)):
            if new_tail[i][0] == self.x and new_tail[i][1] == self.y:
                return True
        return False

    def move (self, event):
        self.last_move = self.tail[-1]
        self.tail[0] = [self.x, self.y]
        if event[pg.K_LEFT] and self.side != 'RIGHT':
            self.side = 'LEFT'
        if event[pg.K_RIGHT] and self.side != 'LEFT':
            self.side = 'RIGHT'
        if event[pg.K_UP] and self.side != 'DOWN':
            self.side = 'UP'
        if event[pg.K_DOWN] and self.side != '':
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

    def update_tail(self):
        if len(self.tail) > 2:
            for i in reversed(range(len(self.tail))):
                self.tail[i] = self.tail[i - 1]

    def add_block(self):
        self.tail.append(self.last_move)

    def update(self):
        self.update_tail()