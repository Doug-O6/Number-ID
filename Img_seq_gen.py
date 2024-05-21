import pygame

number_images = []

def add_list():
  for i in range(0,10):
    #temp = str(i.png)
    number_images.append('Graphics/' + str(i) + '.png')


add_list()
print(number_images)