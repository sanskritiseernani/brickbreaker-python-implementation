# Sanskriti Seernani
# Section 062

from Drawable import Drawable
import pygame


class Ball(Drawable):
    def __init__(self,x,y,visible=True,radius=8):
        super().__init__(x,y,visible)
        self.__radius = radius

    def get_rect(self):
        variable = self.getLoc()
        return pygame.Rect(variable[0] - self.__radius, variable[1] - self.__radius, self.__radius*2, self.__radius*2)

    def draw(self,surface):
        loc = self.getLoc()
        pygame.draw.circle(surface,(220,20,60),(int(loc[0]), int(loc[1])), self.__radius)
