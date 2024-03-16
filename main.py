import pygame as pg
from player import Player
from apple import Apple

HEIGHT = 600
WEIGHT = 600
game_over = True

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((HEIGHT, WEIGHT))
        self.back_surf = pg.image.load('image.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)
        self.Apple = Apple(self.screen)

    def game(self):
        while not self.finish():
            self.draw()
            self.move()
            self.update()
            self.clock.tick(20)
    
    def draw(self):
        self.screen.blit(self.back_surf, (0, 0))
        self.player.draw()
        self.Apple.draw()

    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        key = pg.key.get_pressed()
        self.player.move(key)
    
    def finish(self):
        return self.player.x >= WEIGHT or self.player.x < 0 or self.player.y >= HEIGHT or self.player.y < 0


    def update(self):
        pg.display.update()

game = Game()
game.game()