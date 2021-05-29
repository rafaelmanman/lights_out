import pygame
from random import randint
from board import Board

class Game:
    def __init__(self):
        self.screen_height = 500
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.board = Board()
        self.clicked = False


    def setup(self):
        self.board.clear()
        for i in range(10):
            x = randint(0, 4)
            y = randint(0, 4)
            self.board.change_lights([x, y])

    def getClicked(self):
        for cord, tile in self.board.tile_map.items():
            pos = pygame.mouse.get_pos()
            if tile.collidepoint(pos) and pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.board.change_lights(cord)
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

    def drawText(self, text, size, x, y):
        font = pygame.font.SysFont("Comic Sans", size)
        display_text = font.render(text, True, (255,255,255), (0,0,0)) 
        display_rect = display_text.get_rect() 
        display_rect.center = (x, y) 
        self.screen.blit(display_text, display_rect)

    def drawWinText(self):
        self.screen.fill((0,0,0))
        self.drawText("You Win!", 64, 250, 250)

    def checkWin(self):
        return self.board.isComplete()

    def draw(self):
        self.board.draw(self.screen)

    def run(self):
        self.draw()
        self.getClicked()
