import pygame
from pygame.locals import *
import os

WHITE = (255,255,255)
BLACK = (0,0,0)

BOTTOM = 200

# init piTFT

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

# Init pygame and screen

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

font = pygame.font.Font(None, 36)

class Button:
   def __init__(self,title):
	self.text = font.render(title, 0, WHITE)
	self.bounds = self.text.get_rect()
	self.pos=(0,0)
   def hit(self,pos):
	butpos = self.bounds.move(self.pos)
	return  butpos.collidepoint(pos)

buttons = [
	Button('NASA'),
	Button('Astronomy'),
	Button('Pictures'),
	Button('Photos'),
	Button('Webcam'),
	Button('Camera')]

# show buttons on screen 
x = 0 
y = 0
for button in buttons:
	button.pos = (x,y)
	screen.blit(button.text,(x,y))
	x = x + button.bounds.width + 10
	if (x > 220): 
		x = 0
		y = y + 40

pygame.display.update()

#main loop

while(True):

  # Process touchscreen input
  while True:
    for event in pygame.event.get():
      if(event.type is MOUSEBUTTONDOWN):
        pos = pygame.mouse.get_pos()
	for button in buttons:
		if button.hit(pos):
			pygame.draw.rect(screen,BLACK,(50,BOTTOM,200,50))
			screen.blit(button.text,(50,BOTTOM))
			pygame.display.update()
