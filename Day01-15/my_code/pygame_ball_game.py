from enum import Enum, unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r, g, b)
    

class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True