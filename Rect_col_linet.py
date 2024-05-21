# This Pygame program creates the basic set up for pygame - screen objects, game loop, quit.
# A loop is used to check for collisions between a line and obstacle rectangles.
# In this case, if a collision is detected the obstacle rectangle is switched to a red color.
# The line is created from the center of the screen to the location of the mouse courser.
# No classes are used.
# Using https://www.youtube.com/watch?v=BHr9jxKithk&t=11s

import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rectangle Collision')

# Create all rectangles
obstacles = []
for _ in range(5):
  obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
  obstacles.append(obstacle_rect)

# Creating a line
line_start = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Colors
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Main Game loop
run = True
while run:

  # Update background
  screen.fill(BG)

  # Get mouse position
  pos = pygame.mouse.get_pos()

  # Draw line
  pygame.draw.line(screen, WHITE, line_start, pos, 5)

  # Draw rectangles
  for obstacle in obstacles:
    if obstacle.clipline((line_start, pos)):
      pygame.draw.rect(screen, RED, obstacle)
    else:
      pygame.draw.rect(screen, BLUE, obstacle)

  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # Update display
  pygame.display.flip()

pygame.quit