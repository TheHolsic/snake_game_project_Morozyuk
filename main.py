import pygame as pg
from player import Player
from apple import Apple

HEIGHT = 800
WEIGHT = 800
game_over = True
green = (30, 247, 88)
black = (0, 0, 0)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((HEIGHT, WEIGHT))
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
        self.Apple = Apple(self.screen, self.player)
        self.body = []
        self.score = 1
        self.last_move = None

    def game(self):
        while not self.finish():
            self.draw()
            self.move()
            self.update()
            self.clock.tick(20)
    
    def draw(self):
        self.screen.fill(green)
        self.player.draw()
        self.Apple.draw()
        for i in range(len(self.body)):    
            self.rect = pg.draw.rect(self.screen, black, [self.body[i][0], self.body[i][1], 20, 20])    


    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        key = pg.key.get_pressed()
        self.last_move = [self.player.x, self.player.y]
        self.player.move(key)
        if len(self.body) > 1:
            for i in range(len(self.body) - 1):
                self.body[::-1]
                self.body[i] = self.body[i - 1]
                self.body[0] = [self.last_move]

        print(self.body)
    
    def finish(self):
        return self.player.x >= WEIGHT or self.player.x < 0 or self.player.y >= HEIGHT or self.player.y < 0
    

    def update(self):
        pg.display.update()
        if self.Apple.spawn():
            self.score += 1
            self.body.append([self.last_move])


game = Game()
game.game()