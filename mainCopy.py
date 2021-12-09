import pygame
from ball import Ball
from paddle import Paddle

WHITE = (255, 255, 255)

# Initialize our pygame
pygame.init()
screen_width = 800
screen_size = (screen_width, 600)

# Create our screen, y,x = (width, height)
screen = pygame.display.set_mode(screen_size)

# Title bar and icon
pygame.display.set_caption("Brick Breaker")
icon = pygame.image.load('wall.png')
pygame.display.set_icon(icon)

# Position to start our paddle
paddleX_change = 0
paddleX = (screen_width/ 2) - 45

# Create our blocks
brownBlock = pygame.image.load('brownblock.png')
blueBlock = pygame.image.load('blueblock.png')

paddle = Paddle(WHITE, 10, 100)
paddle.rect.x = 20
paddle.rect.y = 200
def paddle_display(x):
    # rectangle object (display, (RBG), (left, top, width, height), fill/thickness)
    pygame.draw.rect(screen, (255, 255, 255), (x, 550, 90, 15), width=0)


def brown_block(x, y):
    screen.blit(brownBlock, (x, y))


def blue_block(x, y):
    screen.blit(blueBlock, (x, y))


class Wall:
    rows, cols = int(), int()

    def __init__(self, cols, rows, brick_size=64):
        starting_x = (screen_width - (cols * brick_size)) / 2
        x = starting_x
        y = brick_size * 2

        for row in range(rows):
            for col in range(cols):
                brown_block(x, y)
                x += brick_size
            y += brick_size
            x = starting_x


class Ball(pygame.sprite.Sprite):

    def __init__(self, size, x, y):
        super().__init__()
        self.radius = size
        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.velocity = [1.5, 1.5]
        # circle object ((surface, color, center, radius, width)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


all_sprites_list = pygame.sprite.Group()
all_sprites_list.add()

# starting position and speed of ball
ballX_change = 0
ballX = (screen_width / 2)
ballY_change = 0
ballY = 545
ball_at_rest = True

running = True
while running:

    screen.fill((0, 0, 0))
    # Wall(8, 2)
    paddle_launched = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement left and right
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            paddleX_change = -3
        if event.key == pygame.K_RIGHT:
            paddleX_change = 3
        if event.key == pygame.K_UP:
            ball_at_rest = False
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            paddleX_change = 0

    paddleX += paddleX_change

    # Hitting screen edge paddle and ball behavior
    if paddleX <= 0:
        paddleX = 0
    elif paddleX >= 710:
        paddleX = 710
    paddle_display(paddleX)
    # Before launch behavior for ball
    if ball_at_rest:
        ballX += paddleX_change
        if paddleX == 0:
            ballX = 45
        if paddleX == 710:
            ballX = screen_width - 45

    if not ball_at_rest:
        ballY_change = -1.5
        ballX_change = 0
        ballX += ballX_change
        ballY += ballY_change
        pass

    Ball(ballX, ballY)
    pygame.display.update()
