import pygame
from ball import Ball
from paddle import Paddle
from block import Block
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()
screen_width = 800
screen_size = (screen_width, 600)

# Create the screen, (width, height)
screen = pygame.display.set_mode(screen_size)

# Title bar and icon
pygame.display.set_caption("Brick Breaker")
icon = pygame.image.load('wall.png')
pygame.display.set_icon(icon)

# At start position paddle in center of screen
paddle_center_x = (screen_width/2) - 50

# Initialize paddle
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = paddle_center_x
paddle.rect.y = 550

# Initialize a ball
ball = Ball(WHITE, 14)
ball_at_rest = True

# Create and add player sprites to a list of All Sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# Create a matrix to base our wall on
block_sprites = pygame.sprite.Group()
brick_width = 100
brick_height = 20
wall_length = 6
color_dict = {
    0:"aquamarine",
    1:"cadetblue",
    2:"cadetblue4",
    3:"aquamarine3",
    4:"aquamarine4",
    5:"aliceblue",
    6:"antiquewhite",
    7:"azure",
    8:"azure3",
}
wall_design = np.random.randint(4, size=(4, 6))
# Build wall with blocks from Block class
def build_wall(design = wall_design):
    for row_idx, row in enumerate(design):
        for col_idx, val in enumerate(row):
            color = color_dict[val]
            block = Block(color, brick_width, brick_height)
            block.rect.x = (brick_width * col_idx) + brick_width
            block.rect.y = (brick_height * row_idx) + brick_height * 4
            block_sprites.add(block)
            all_sprites_list.add(block)

# Initialize a pre-game state
background = pygame.image.load("space.jpg")
clock = pygame.time.Clock()
level = 1
score = 0
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True:  # Infinite loop that will be broken when the user press the space bar again
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break  # Exit infinite loop
    # Set text size and style
    font = pygame.font.Font(None, 54)

    # Paddle action and ball_at_rest action
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(10)
    if keys[pygame.K_UP]:
        ball_at_rest = False

    all_sprites_list.update()

    if ball_at_rest:
        # Have ball move with paddle
        ball.rect.x = paddle.rect.x + 50
        ball.rect.y = paddle.rect.y - 15
        # Display instruction and level
        level_text = font.render("Level " + str(level), 1, WHITE)
        start_text = font.render("Press Up Arrow to Start", 1, WHITE)
        pause_text = font.render("and Space Bar to Pause", 1, WHITE)
        screen.blit(level_text, (330, 250))
        screen.blit(start_text, (200, 300))
        screen.blit(pause_text, (200, 350))
        if level == 1:
            build_wall()


    if not ball_at_rest:
        ball.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 780:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y > 600:
        score = 0
        ball_at_rest = True

    # Bounce ball when collides with paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()

    # Collision of ball with brick
    if pygame.sprite.spritecollide(ball, block_sprites, dokill=True):
        score += 1
        ball.bounce()

    # Draw all sprites
    all_sprites_list.draw(screen)

    # Display score
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 570))

    # Update the screen
    pygame.display.flip()

    # Run at 60 frames per second
    clock.tick(60)

pygame.quit()


