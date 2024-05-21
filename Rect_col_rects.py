# This Pygame program creates the basic set up for pygame - screen objects, game loop, quit.
# The program then creates a rectangle that is moved by the curser and 5 "obstacle" rectangles.
# A loop is used to check for collisions between the main rectangle and obstacle rectangles.
# In this case, if a collision is detected the main rectangle is switched to a red color.
# A line is then added (49) that prints the list number of the rectangle collided with.
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
rect_1 = pygame.Rect(0,0,25,25)

obstacles = []
for _ in range(5):
  obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
  obstacles.append(obstacle_rect)

print(obstacles)

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
  #for obstacle in obstacles:
  #  if rect_1.colliderect(obstacle):
  #    col = RED
  #<< using pygame function >>
  if rect_1.collidelist(obstacles) >= 0:
    print(rect_1.collidelist(obstacles))
    col = RED

  # Get mouse coordinates and use them to position the rectangle
  pos = pygame.mouse.get_pos()
  rect_1.center = pos

  # Draw rectangles
  pygame.draw.rect(screen, col, rect_1)
  for obstacle in obstacles:
    pygame.draw.rect(screen, BLUE, obstacle)

  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # Update display
  pygame.display.flip()

pygame.quit