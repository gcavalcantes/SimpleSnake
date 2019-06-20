"""
Main file

File responsible for everything
"""


import pygame
import random
from pygame.locals import *

# Funcion to randomize the apple position
def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x//10 * 10, y//10 * 10

# Test the collision between two cells
def collision(c1, c2):
    # Return true if the two compared cells are in the same position
    return (c1[0] == c2[0] and (c1[1] == c2[1]))

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Create a screen to display
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

# Creates snake
snake = [(200, 200), (210, 210), (220, 220)]
# Defines the skin color for the snake
snake_skin = pygame.Surface((10, 10))
# Fill snake with the black color
snake_skin.fill((255, 255, 255))

# Set the apple position
apple_pos = on_grid_random()
# Creates apple
apple = pygame.Surface((10, 10))
# Fill apple with the red color
apple.fill((255, 0, 0))

my_direction = LEFT

# Game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Ticks the game clock
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    # Checks collision with apple
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    # TODO check collision with wall

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,   snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()