import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, size):
        super().__init__()

        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([size, size])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        # circle object ((surface, color, center, radius, width)
        pygame.draw.circle(self.image, color, ((size / 2), (size / 2)), (size / 2))

        self.velocity = [randint(-4, 4), randint(-6, 6)]

        # Fetch the circle object that sits within the dimensions of the image.
        self.rect = self.image.get_rect()

    def launch(self):
        self.rect.x = 0
        self.rect.y = -5

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = randint(-6, 6)
        self.velocity[1] = -randint(1, 6)

