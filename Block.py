# Sanskriti Seernani
# Section 062

from Drawable import Drawable
import pygame


class Block(Drawable):
    def __init__(self,x,y,visible=True,side=20):
        super().__init__(x,y,visible)
        self.__side = side

    def get_rect(self):
        variable = self.getLoc()
        return pygame.Rect(variable[0], variable[1], self.__side, self.__side)

    def draw(self,surface):
        pygame.draw.rect(surface,(0,0,255),self.get_rect())
        pygame.draw.rect(surface, (0, 0, 0), self.get_rect(),2)

