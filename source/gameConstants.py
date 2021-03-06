from enum import Enum
import pygame

pygame.font.init()
#infoObject = pygame.display.Info()

class Color(Enum):
	BLACK = (0,0,0)
	WHITE = (255, 255, 255)
	RED = (175, 39, 29)
	GREEN = (57, 160, 85)
	BRIGHT_GREEN = (70, 206, 107)
	BRIGHT_RED = (224, 48, 35)


class Dimensions(Enum):
	WIDTH = 800
	HEIGHT = 600
	PLAYER_FRAME = 6


class Fonts(Enum):
	BASICFONT = pygame.font.SysFont(None, 50)
	SMALLFONT = pygame.font.SysFont(None, 25)

class Sounds(Enum):
        SpiderSqueak = "spiderSqueak.wav"
