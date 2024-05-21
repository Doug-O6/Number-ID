import pygame, sys

# Class -----------------------------------
class Crosshair(pygame.sprite.Sprite):
  def __init__(self, width, height,pos_x, pos_y, color):
    super().__init__()
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.center = [pos_x,pos_y]

# -------------------------------------------

# General setup
pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

# Game screen
screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# Object creation
crosshair = Crosshair(50,50,100,100,(255,255,255))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit
      sys.exit()


  pygame.display.flip()
  crosshair_group.draw(screen)
  clock.tick(60)