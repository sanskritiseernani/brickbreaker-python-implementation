# Sanskriti Seernani
# Section 062

import pygame
import abc


class Drawable(metaclass=abc.ABCMeta):
    def __init__(self,x,y,visible=True):
        self.__x = x
        self.__y = y
        self.__visible = visible

    def getLoc(self):
        return self.__x, self.__y

    def setLoc(self,p):
        self.__x = p[0]
        self.__y = p[1]

    def getVisible(self):
        return self.__visible

    def setVisible(self,v):
        self.__visible = v

    @abc.abstractmethod
    def draw(self,surface):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass
