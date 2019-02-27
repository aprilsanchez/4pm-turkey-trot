import time, pygame
from gameConstants import Color, Dimensions


class Player:
    def __init__(self, x=50, y=450):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 25, 50)
        self.events = []
        self.pressed = None
        self.health = 100
        self.score = 0
        self.immune_time = 0
        # self.image = pygame.Surface([x, y], pygame.SRCALPHA)
        # self.image = pygame.image.load("player.png").convert_alpha()
        self.index = 0
        self.state = 0
        #        self.transparent = self.image.get_at((0,0))
        #        print(self.transparent)
        #       print(Color.BLACK.value)
        #       self.image.set_colorkey(self.transparent)

        #        self.rect = self.image[self.index].get_rect()
        # this line from original code

    def update(self, events):
        self.events = events

    def move(self, direction):
        if self.state == 0:
            self.state += 1
            self.index += 1
        else:
            self.state = 0
        if self.index >= Dimensions.PLAYER_FRAME.value:
            self.index = 0

        if direction == 'left' and self.x >= 10:
            self.x -= 10
        elif direction == 'right' and self.x < 780:
            self.x += 10
        self.rect = pygame.Rect(self.x, self.y, 25, 50)

    def hit(self):
        if time.time() - self.immune_time >= 3:
            self.health -= 20
            self.immune_time = time.time()
        return self.health <= 0

    def pick(self):
        self.score += 1
        return self.score

    def refresh(self, events):
        self.update(events)
