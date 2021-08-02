#guided oop snake game

import pygame
from pygame.locals import *


class Snake:
    def __init__(self, window):
        self.window= window
        self.block_img= pygame.image.load("block.jpg").convert()  #loading block
        self.block_X=100
        self.block_Y=100

    def draw(self):
        self.window.fill((110,115,100))    #surface color
        self.window.blit(self.block_img, (self.block_X, self.block_Y))  #updating  block position in surface
        pygame.display.update()    #showing surface with  block

    def move_left(self):
        self.block_X-=10
        self.draw()
    
    def move_right(self):
        self.block_X+=10
        self.draw()

    def move_up(self):
        self.block_Y-=10
        self.draw()
    
    def move_down(self):
        self.block_Y+=10
        self.draw()


class Game:
    def __init__(self):
        pygame.init()   #iniitalizing pygame
        self.window= pygame.display.set_mode((500, 500))  #creating surface
        self.window.fill((110,115,100))  #surface color
        self.snake= Snake(self.window)
        self.snake.draw()

    def run(self):
        running= True
        while running:
            for event in pygame.event.get():
                if event.type== KEYDOWN:
                    if event.key== K_ESCAPE:
                        running=False
                    elif event.key== K_LEFT:
                        self.snake.move_left()
                    elif event.key==K_RIGHT:
                        self.snake.move_right()
                    elif event.key==K_UP:
                        self.snake.move_up()
                    elif event.key==K_SPACE:
                        self.snake.move_down()
                elif event.type== QUIT:
                    running=False

    
if __name__== "__main__":
    game=Game()
    game.run()

