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
import random

#Load files
floor = pygame.image.load('floor.png')
boxImage = pygame.image.load('box.png')
gooberLeft = pygame.image.load('gooberLeft.png')
gooberRight = pygame.image.load('gooberRight.png')
gooberDown = pygame.image.load('gooberDown.png')
gooberUp = pygame.image.load('gooberUp.png')
goal = pygame.image.load('goal.png')


#Define the goober class
class goober:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.rect = pygame.rect.Rect((self.x, self.y, 32, 32))
    self.spriteDirection = 'r'
  
  def movement(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      self.x -= 5
      self.spriteDirection = 'l'
    if key[pygame.K_d]:
      self.x += 5
      self.spriteDirection = 'r'
    if key[pygame.K_w]:
      self.y -= 5
      self.spriteDirection = 'u'
    if key[pygame.K_s]:
      self.y += 5
      self.spriteDirection = 'd'

    self.rect.x = self.x
    self.rect.y = self.y

  def render(self, surface):
    if self.spriteDirection == 'l':
      surface.blit(gooberLeft,(self.x,self.y))
    elif self.spriteDirection == 'r':
      surface.blit(gooberRight,(self.x,self.y))
    elif self.spriteDirection == 'u':
      surface.blit(gooberUp,(self.x,self.y))
    elif self.spriteDirection == 'd':
      surface.blit(gooberDown,(self.x,self.y))
  
  def getRect(self):
    return self.rect
  def getDirection(self):
    return self.spriteDirection


#Define the box class
class box:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.rect = pygame.rect.Rect((self.x, self.y, 32, 32))

  def render(self, surface):
    pygame.draw.rect(surface, (0, 0, 128), self.rect)
    surface.blit(boxImage,(self.x,self.y))

  def getRect(self):
    return self.rect
  
  def push(self,x,y):
    self.x += x
    self.y += y

    self.rect.x = self.x
    self.rect.y = self.y


class goalMaker():
  def __init__(self):
    self.x = random.randint(0,224)
    self.y = random.randint(0,224)
    self.rect = pygame.rect.Rect((self.x, self.y, 32, 32))
  def getRect(self):
    return self.rect
  def render(self, surface):
    pygame.draw.rect(surface, (0, 0, 128), self.rect)
    surface.blit(goal,(self.x,self.y))
  def generate(self):
    self.x = random.randint(0,480)
    self.y = random.randint(0,480)
    self.rect.update((self.x, self.y, 32, 32))


def textDrawer(text,font,color,screen,x,y):
  rendered = font.render(text,True,color)
  screen.blit(rendered,(x,y))


def boxPusherMain():
  #Display setup
  pygame.display.init()
  gameScreen = pygame.display.set_mode((512,512))
  pygame.display.get_surface()

  clock = pygame.time.Clock()
  pygame.init()

  font = pygame.font.SysFont('Arial',14)
  #Create instances of objects
  player = goober(50,50)
  crate = box(100,100)
  target = goalMaker()

  #Main loop
  score = 0
  gameCont = 0
  while gameCont == 0:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          gameCont = 1

    #Events and collision
    player.movement()

    spriteDirection = player.getDirection()

    if pygame.Rect.colliderect(player.getRect(), crate.getRect()): #box and player (use the player's direction to decide which way to push the box)
      if spriteDirection == 'l':
        crate.push(-5,0)
      elif spriteDirection == 'r':
        crate.push(5,0)
      elif spriteDirection == 'u':
        crate.push(0,-5)
      elif spriteDirection == 'd':
        crate.push(0,5)

    #if pygame.Rect.colliderect(): #wall and player (use the player's direction to decide which way to pushback the player)

    #if pygame.Rect.colliderect(): #box and wall

    if pygame.Rect.colliderect(crate.getRect(), target.getRect()): #box and goal
      target.generate()
      score += 1

    #Rendering
    #Render the floor with two loops
    floorRenderX = 0
    floorRenderY = 0
    loopY = 0
    loopX = 0
    while loopY < 16:
      while loopX < 16:
        gameScreen.blit(floor,(floorRenderX,floorRenderY))
        floorRenderX += 32
        loopX += 1
      floorRenderY += 32
      loopX = 0
      floorRenderX = 0
      loopY += 1

    crate.render(gameScreen)
    target.render(gameScreen)
    player.render(gameScreen)

    textDrawer(f'Score: {score}',font,(0,0,0),gameScreen,150,0)
    
    pygame.display.flip()
    clock.tick(60)

#MAKE SURE TO CLOSE ALL YOUR FILES!!!
boxPusherMain()