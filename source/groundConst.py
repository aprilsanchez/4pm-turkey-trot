# groundData.py
from enum import Enum
import pygame
from gameConstants import Dimensions

pygame.init()
pygame.font.init()

h = (4 / 5) * Dimensions.HEIGHT.value
y0 = 0
y1 = Dimensions.HEIGHT.value * (1 / 2)
s1 = 1


# syntax: groundNum = [ [List of food objects], [List of vertical Spiders], [List of horizontal Spiders]] -> parameters for Object and Spider constructors
# [List of food objects] = [ (object0_x_pos, object0_y_pos),(object1_x_pos, object1_y_pos), ...]
# [List of vertical spiders] = [ (spider0_x_pos, spider0_speed, spider0_y_pos),(spider1_x_pos, spider1_speed, spider1_y_pos), ...]
# [List of horizontal spiders] = [ (speed, spider0_x_start, spider0_x_end), (speed, spider1_x_start, spider1_x_end), ...]


class LevelOne(Enum):
    ground0 = [[(100, h), (225, h), (325, h), (425, h), (525, h), (625, h), (725, h)],
               [(150, 1, y0), (300, 1, y1), (500, 1, y0), \
                (700, 1, y1)], []]

    ground1 = [[(150, h), (300, h), (450, h), (600, h), (750, h)], [(150, 1, y0), (400, -1, 400), (750, 1, y0)],
               [(1, 150, 700)]]

    ground2 = [[(100, h), (200, h), (300, h), (400, h), (500, h), (600, h), (700, h)], [],
               [(1, 100, 300), (1, 300, 500), (1, 500, 700)]]

    ground3 = [[(150, h), (300, h), (450, h), (600, h), (750, h)],
               [(146, 1, 17), (269, 2, 56), (449, 1, y0), (690, 2, 50)], [(1, 200, 700)]]

    ground4 = [[(75, h), (150, h), (225, h), (300, h), (375, h), (450, h), (525, h), (600, h), (675, h), (750, h)], \
               [(100, 1, y0), (200, 1, y0), (280, 3, y0), (350, 2, y0), (440, 1, y0), (510, 2, y0), (570, 3, 123), \
                (690, 2, 50)], []]

    ground5 = [[(75, h), (150, h), (225, h), (300, h), (375, h), (450, h), (525, h), (600, h), (675, h), (750, h)], \
               [(173, 1, 176), (217, 1, 27), (380, 2, y0), (488, 1, y0), (570, 2, 123), \
                (690, 2, 50)], [(1, 125, 725)]]

    ground6 = [[(100, h), (200, h), (300, h), (400, h), (500, h)], \
               [(100, 1, y0), (140, 1, y0), (180, 1, y0), (260, 1, 75), (300, 1, 75), (340, 1, 75), (420, 1, 150),
                (460, 1, 150), (500, 1, 150), \
                (580, 1, 225), (620, 1, 225), (660, 1, 225)], []]

    ground7 = [[(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h)], \
               [(120, 1, y0), (180, 2, y0), (240, 1, y0), (300, 2, y0), (360, 1, y0), (420, 2, y0), (480, 1, y0),
                (540, 2, y0), (600, 1, y0), \
                (660, 2, y0), (720, 1, y0), (780, 2, y0)], []]
    ground8 = [[(200, h), (350, h), (500, h)], \
               [(100, 1, y0), (150, 1, y0), (200, 1, y0), (250, 2, y1), (300, 2, y1), (350, 2, y1), (400, 1, y0),
                (450, 1, y0), (500, 1, y0), \
                (550, 2, y1), (600, 2, y1), (650, 2, y1), (700, 1, y0), (750, 1, y0), (800, 1, y0)], []]

    ground9 = [[(100, h), (225, h), (325, h), (425, h), (525, h), (625, h), (725, h)],
               [(150, -2, y0), (210, -2, 40), (270, -2, 80), (330, -2, 120), (390, -2, 160), (450, -2, 200),
                    (510, -2, 240), (570, -2, 280), \
                    (630, -2, 320), (690, -2, 360), (750, -2, 400)], []]

    ground10 = [[(100, h), (175, h), (300, h), (550, h), (250, h)], \
                [(100, s1, 0), (125, s1, 40), (150, s1, 80), (175, s1, 120), (200, s1, 160), (225, s1, 200),
                 (250, s1, 240), (275, s1, 280), (300, s1, 320), \
                 (325, s1, 360), (350, s1, 400), (375, s1, 440), (400, s1, 480), (425, s1, 440), (450, s1, 400),
                 (475, s1, 360), (500, s1, 320), \
                 (525, s1, 280), (550, s1, 240), (575, s1, 200), (600, s1, 160), (625, s1, 120), (650, s1, 80),
                 (675, s1, 40), (700, s1, 0)], []]

    ground11 = [[(100, h), (225, h), (325, h), (425, h), (525, h), (625, h), (725, h)],
                [(100, 1, 400), (125, 1, 320), (150, 1, 240), (175, 1, 160), (200, 1, 80), (225, 1, y0), (250, 1, 80),
                 (275, 1, 160), (300, 1, 240), \
                 (325, 1, 320), (350, 1, 400), (450, 1, y0), (475, 1, 80), (500, 1, 160), (525, 1, 240), (550, 1, 320),
                 (575, 1, 400), (600, 1, 320), \
                 (625, 1, 240), (650, 1, 160), (675, 1, 80), (700, 1, y0)], []]

    g = [
            #level one
            [ground0, ground1, ground2, ground3],
            #level two
            [ground4, ground5, ground6, ground7],
            #level three
            [ground8, ground9, ground10, ground11]
        ]


