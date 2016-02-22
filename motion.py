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

host = "cctv"
port = 8081
webcam = "/run/shm/webcam.jpg"

# Init framebuffer/touchscreen environment variables
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

# Get user & group IDs for file & folder creation
# (Want these to be 'pi' or other user, not root)
s = os.getenv("SUDO_UID")
uid = int(s) if s else os.getuid()
s = os.getenv("SUDO_GID")
gid = int(s) if s else os.getgid()

# Init pygame and screen
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

def getmjpeg():
 # from https://gist.github.com/russss/1143799

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 try:
     s.connect((host, int(port)))
 except socket.error, msg:
            print "Couldnt connect with the server: %s\n " % msg
            return

 fh = s.makefile()

 # Read in HTTP headers:
 line = fh.readline()
 while line.strip() != '': 
    parts = line.split(':')
    if len(parts) > 1 and parts[0].lower() == 'content-type':
        # Extract boundary string from content-type
        content_type = parts[1].strip()
        boundary = content_type.split(';')[1].split('=')[1]
    line = fh.readline()

 if not boundary:
    raise Exception("Can't find content-type")

 # Seek ahead to the first chunk
 while line.strip() != boundary:
    line = fh.readline()

 # Read in chunk headers
 while line.strip() != '': 
    parts = line.split(':')
    if len(parts) > 1 and parts[0].lower() == 'content-length':
        # Grab chunk length
        length = int(parts[1].strip())
    line = fh.readline()

 image = fh.read(length)

 with open(webcam, 'w') as out_fh:
     out_fh.write(image)
 
 s.close()

# Main loop ----------------------------------------------------------------

screenMode = 0

while(True):

  # Process touchscreen input
  while True:
    for event in pygame.event.get():
      if(event.type is MOUSEBUTTONDOWN):
        pos = pygame.mouse.get_pos()
    break


  getmjpeg()
  
  img      = pygame.image.load(webcam)
  scaled   = pygame.transform.scale(img, (320,240))

  # Refresh display
  img = scaled       # Show last-loaded image

  if img is None or img.get_height() < 240: # Letterbox, clear background
    screen.fill(0)
  if img:
    screen.blit(img,
      ((320 - img.get_width() ) / 2,
       (240 - img.get_height()) / 2))

  pygame.display.update()
  time.sleep(1)

