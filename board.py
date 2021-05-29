import pygame

class Board:
    def __init__(self):
        self.board = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.tile_size = 98
        self.tile_map = {}

    def clear(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                self.board[y][x] = 0

    def draw(self, screen):
        screen.fill((255,255,255))
        black = (0,0,0)
        green = (0, 200, 0)
        colors = [black, green]
        tile_size = self.tile_size
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                value = self.board[i][j]
                rect = pygame.Rect(j*(tile_size+2), i*(tile_size+2), tile_size, tile_size)
                pygame.draw.rect(screen, colors[value], rect)
                self.tile_map[(j,i)] = rect

    def isComplete(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    return False
        return True

    def toggle(self, x, y):
        value = self.board[y][x]
        self.board[y][x] = [1,0][value]

    def change_lights(self, cord):
        x, y = cord
        self.toggle(x, y)
        if y>0:
            self.toggle(x, y-1)
        if x<4:
            self.toggle(x+1, y)
        if y<4:
            self.toggle(x, y+1)
        if x>0:
            self.toggle(x-1, y)
