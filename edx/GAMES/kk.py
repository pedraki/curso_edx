import pygame


pygame.init()

width, height = 700,700 
screen=pygame.display.set_mode((height,width))
mouseClick=pygame.mouse.get_pressed()
print(type(mouseClick))
d,i,c =mouseClick
print (d,i,c)
print(mouseClick[2])