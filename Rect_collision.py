# This Pygame program creates the basic set up for pygame - screen objects, loop, quit.
# The program then creates 2 rectangles and a condition to detect a collision between them.
# If a colliion is detected, then whatever you wan done can be added.  
# In this case the obstacle rectangle is move to the lower left corner and made larger.
# No classes are used.
# Using https://www.youtube.com/watch?v=BHr9jxKithk&t=11s

import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rectangle Collision')

# Create main rectangle and obstacle rectangles
rect_1 = pygame.Rect(0,0,25,25)
obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)

# Colors
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Hide mouse
pygame.mouse.set_visible(False)

# Game loop
run = True
while run:

  # Update background
  screen.fill(BG)

  # Set color
  col = GREEN
  if rect_1.colliderect(obstacle_rect):
    obstacle_rect = pygame.Rect(500, 300, 50, 30)

  # Get mouse coordinates and use them to position the rectangle
  pos = pygame.mouse.get_pos()
  rect_1.center = pos

  # Draw rectangles
  pygame.draw.rect(screen, col, rect_1)
  pygame.draw.rect(screen, BLUE, obstacle_rect)

  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # Update display
  pygame.display.flip()

pygame.quit