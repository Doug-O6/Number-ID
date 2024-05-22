# This Pygame program places numbers randomly across the screen.  A green rectangle is moved
# by the mouse.  If there is a collision between the rectangle and one of the numbers, then
# the number is moved to a location in the sequence of numbers 0 through 9.  
# To be added: Make it so that "winning" the game is achieved by colliding with the numbers
# in sequence.  Should add intro screen too.
# No classes are used.
# Using https://www.youtube.com/watch?v=BHr9jxKithk&t=11s, https://www.youtube.com/watch?v=ndtFoWWBAoE

import pygame
import random

# Functions ---------------------------------------------------------------------
def text_image_gen(text, font, text_col):
  """
  Function converts a text string into an image of the text so it can be displayed in pygame.
  A rectangle is also generated for detecting  collisions in the game.  The rectangles are placed
  at random location at the start of the game The images and associated rectangles are placed in 
  separate lists.
  """
  img = font.render(text, True, text_col)
  num_img_list.append(img)
  img_rect = img.get_rect(center = (random.randint(100,700), random.randint(200,500)))
  num_rect_list.append(img_rect)

def num_seq_lst_gen(text, font, text_col, x, y):
  """This function does the same as above but places the rectangles at predetermined fixed locations."""
  img = font.render(text, True, text_col)
  num_seq_img_lst.append(img)
  img_rect = img.get_rect(center = (x, y))
  num_seq_rect_list.append(img_rect)


def draw_text(text, font, text_col, x, y):
  """This function converts a text string into an image and puts in on the screen"""
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
# ---------------------------------------------------------------------------
# Initiate pygame
pygame.init()

text_font = pygame.font.SysFont("Arial", 50)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Display setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Koen's Number ID Game")

# Create curser rect
curser_rect = pygame.Rect(0,0,20,20)

# Sounds -----------------
sound_1 = pygame.mixer.Sound('Sounds/retro-game.wav')
applause = pygame.mixer.Sound('Sounds/applause.wav')


# Generate a list of integer number images at random locations
num_img_list = []
num_rect_list = []
text_image_gen("0", text_font, (255, 255, 255))
text_image_gen("1", text_font, (255, 0, 0))
text_image_gen("2", text_font, (77, 166, 255))
text_image_gen("3", text_font, (255, 255, 77))
text_image_gen("4", text_font, (255, 75, 255))
text_image_gen("5", text_font, (255, 204, 255))
text_image_gen("6", text_font, (255, 255, 0))
text_image_gen("7", text_font, (230, 76, 0))
text_image_gen("8", text_font, (0, 0, 255))
text_image_gen("9", text_font, (0, 255, 0))

# Generate list of numbers with positions in order at top of screen
num_seq_img_lst = []
num_seq_rect_list = []
y = 125
num_seq_lst_gen("0", text_font, (255, 255, 255), 200, y)
num_seq_lst_gen("1", text_font, (255, 0, 0), 240, y)
num_seq_lst_gen("2", text_font, (77, 166, 255), 280, y)
num_seq_lst_gen("3", text_font, (255, 255, 77), 320, y)
num_seq_lst_gen("4", text_font, (255, 75, 255), 360, y)
num_seq_lst_gen("5", text_font, (255, 204, 255), 400, y)
num_seq_lst_gen("6", text_font, (255, 255, 0), 440, y)
num_seq_lst_gen("7", text_font, (230, 76, 0), 480, y)
num_seq_lst_gen("8", text_font, (0, 0, 255), 520, y)
num_seq_lst_gen("9", text_font, (0, 255, 0), 560, y)

# Hide mouse -----
pygame.mouse.set_visible(False)


# Game loop -------------- Game loop --------------------------------
run = True
while run:

  # Update background
  screen.fill((50, 50, 50))

  # Print game name to the screen
  draw_text("Koen's Number Finding Game", text_font, (255, 255, 255), 125, 25)

  # Draw numbers at random places on screen.
  for i in range(0,10):
    screen.blit(num_img_list[i], num_rect_list[i])

  # Draw curser rect
  pygame.draw.rect(screen, (0, 255, 0), curser_rect)

  # Get mouse coordinates and use them to position the rectangle
  pos = pygame.mouse.get_pos()
  curser_rect.center = pos

  # Change number position when curser rect collides with number rect and play "bleep" sound
  # when number moves. Play applause when 9 is chosen.
  num = curser_rect.collidelist(num_rect_list)

  if num >= 0:
    #print(f"First print {num}")
    sound_1.play()
    num_rect_list[num] = num_seq_rect_list[num]

    if num == 9:
      applause.play()
  
  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # Update display
  pygame.display.update()

pygame.quit