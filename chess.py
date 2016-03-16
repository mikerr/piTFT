# Display the mjpeg stream of motion server on piTFT screen

import io
import os
import pygame
import time
from pygame.locals import *
from subprocess import call  

import socket
import sys 

# Initialization -----------------------------------------------------------

# Init framebuffer/touchscreen environment variables
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

# Init pygame and screen
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


screenMode = 0

pos = (20,20)


file = "./images/b.png"
backb      = pygame.image.load(file)
file = "./images/w.png"
backw      = pygame.image.load(file)

# draw board

scale = 29

def drawboard ():

 white = 0
 black = 1
 color = white

 for x in range (0,8):
    color = 1 - color
    for y in range (0,8):
	if (color == white):
		screen.blit(backw,(x * scale,y * scale ))
		color = black;
	else:
		screen.blit(backb,(x * scale,y * scale ))
		color = white;

font = pygame.font.Font(None, 36)
piece = font.render("K", 1, (255, 255, 255))

drawboard()

# Main loop ----------------------------------------------------------------

while(True):

  # Process touchscreen input
  while True:
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
           pos = pygame.mouse.get_pos()
  	   x = pos[0] / scale
  	   y = pos[1] / scale
	   drawboard()
	   screen.blit (piece,(x*scale,y*scale))
    break


  pygame.display.update()
  time.sleep(0.1)

