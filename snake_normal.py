import pygame     #importing pygame library
from pygame.locals import *   #for using keyboard 


def draw_block():
    window.fill((110,115,100))    #surface color
    window.blit(block_img, (block_X, block_Y))  #updating  block position in surface
    pygame.display.update()    #showing surface with  block



if __name__=="__main__":
    pygame.init()   #iniitalizing pygame
    window= pygame.display.set_mode((500, 500))  #creating surface
    pygame.display.set_caption("Snake Game")
    window.fill((110,115,100))  #surface color
    

    block_img= pygame.image.load("block.jpg").convert()  #loading block
    block_X=100;block_Y=100    #coordinate of block in surface at begining
    window.blit(block_img, (block_X, block_Y))  #adding block in surface at begining
    pygame.display.update()   # initial showing surface and block

    running= True
    while running:
        for event in pygame.event.get():
            if event.type== KEYDOWN:
                if event.key== K_ESCAPE:
                    running=False
                elif event.key== K_LEFT:
                    block_X+=10
                    draw_block()
                elif event.key==K_RIGHT:
                    block_X-=10
                    draw_block()
                elif event.key==K_UP:
                    block_Y-=10
                    draw_block()
                elif event.key==K_SPACE:
                    block_Y+=10
                    draw_block()

            elif event.type== QUIT:
                running=False


