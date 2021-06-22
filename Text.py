# Sanskriti Seernani
# Section 062

from Drawable import Drawable
import pygame


class Text(Drawable):
    def __init__(self, x, y, visible=True, score=0, message="SCORE: ", color =(0,0,0)):
        super().__init__(x, y, visible)
        self.__score = score
        self.__font = pygame.font.SysFont("timesnewroman",30)
        self.__message = message
        self.__color = color

    def getScore(self):
        return self.__score

    def setScore(self,s):
        self.__score = s

    def get_rect(self):
        pass

    def draw(self,surface):
        canvas = self.__font.render(self.__message + str(self.__score), True, self.__color)
        surface.blit(canvas,(0,0))

