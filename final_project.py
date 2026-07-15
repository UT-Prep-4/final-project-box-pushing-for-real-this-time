#Name(s):
#Final Project - Build Something Worth Showing Off
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: A puzzle game where the player pushes a box into a goal
  THE PIECES I NEED TO BUILD:
  - Player object
  - Box object
  - Goal object
  - Walls object
  - functions to intialize each level
  - Retry functionality 

  WHAT I WILL DEMO AT SHOWCASE: I will through the 3 or so levels, and I will make to fail one so I can showcase the retry functionality

==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''
import pygame
from PIL import Image
#Load files
floor = pygame.image.load('floor.png')
gooberImage = pygame.image.load('gooberRight.png')

#Define the goober class
class goober:
  def __init__(self,x,y,rect):
    self.x = x
    self.y = y
    self.rect = rect
  
  def up(self):
    self.y += 32
  def rt(self):
    self.x += 32
  def dn(self):
    self.y -= 32
  def lt(self):
    self.y -= 32


def levelOneSetUp():
  #make it spawn in all the rects/wall objects for collsion (wall is rect that stops you, box is rect that moves when player pushes it)
  print('')

def boxPusherMain():
  #Display setup
  pygame.display.init()
  gameScreen = pygame.display.set_mode((256,256))
  pygame.display.get_surface()

  clock = pygame.time.Clock()
  
  #Create instances of objects
  player = goober(50,50,70)

  print('WASD to move')

  #Main loop
  gameCont = 0
  while gameCont == 0:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          gameCont = 1
    
    gameScreen.fill("purple")
    rect = pygame.Rect(100, 100, 101, 101)
    gameScreen.blit(floor,(0,0))

    if str(pygame.event.get()).find('w') >= 0:
      player.up
      print(player.y)

    pygame.display.flip()
    clock.tick(60)

#MAKE SURE TO CLOSE ALL YOUR FILES!!!
boxPusherMain()