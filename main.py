import pygame
from game import Game

pygame.init()
done = False
game = Game()

game.setup()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.setup()

    if game.checkWin() == False:
        game.run()
    else:
        game.drawWinText()

    pygame.display.flip()
