import pygame
BLACK = (0, 0, 0)


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.width = width
        self.height = height
        self.color = color

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
