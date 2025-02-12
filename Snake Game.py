import pygame
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Food settings
food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
food_spawn = True

# Game settings
speed = 15
clock = pygame.time.Clock()

# Game Over function
def game_over():
    pygame.quit()
    quit()

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not change_to == 'DOWN':
                    change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                if not change_to == 'UP':
                    change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                if not change_to == 'RIGHT':
                    change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                if not change_to == 'LEFT':
                    change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP':
        snake_direction = 'UP'
    if change_to == 'DOWN':
        snake_direction = 'DOWN'
    if change_to == 'LEFT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT':
        snake_direction = 'RIGHT'

    # Move snake
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    food_spawn = True

    # Background
    screen.fill(BLACK)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT-10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    pygame.display.update()
    clock.tick(speed)

pygame.quit()