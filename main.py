#import libraries
from codecs import xmlcharrefreplace_errors
from telnetlib import XDISPLOC
import pygame
from pygame.locals import *
import sys

#init pygame
pygame.init()

#gloabal variable
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
timer = pygame.time.Clock()
vec =pygame.math.Vector2

#background
bg = pygame.transform.scale(pygame.image.load("bg.png"), size)
clouds = pygame.transform.scale(pygame.image.load("clouds.gif"), (200,200))
i=-720*2

# platforms
class platform(pygame.sprite.Sprite):
    def __init__(self, xloc,yloc):
        pygame.sprite.Sprite.__init__(self)
        self.surf =  pygame.image.load("platform.png")
        self.rect = self.surf.get_rect()
        self.rect.x = xloc 
        self.rect.y = yloc
    
    

p1 = platform(600, 400)
platforms = pygame.sprite.Group()
platforms.add(p1)

#player
ACC = 0.5
FRIC = -0.12
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.image.load("player.png")
        self.rect = self.surf.get_rect()
   
        self.pos = vec((640, 400))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
            hits = pygame.sprite.spritecollide(player , platforms, False)
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
 
    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_UP] and self.pos.y == 435:
            self.vel.y = -10
             
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width
        if self.pos.y > 435:
            self.pos.y =435

        

player = Player() 



#update loop 
while True:
    #background control
    screen.blit(bg, (0,0))
    screen.blit(clouds, (i,0))
    screen.blit(clouds,(width+i,0))
    if (i== width):
        screen.blit(clouds,(width+i,0))
        i=-720*2
    i+=2

    #playerdisplay
    screen.blit(player.surf, player.pos)
    player.move()

    #platform displaytest 
    screen.blit(p1.surf, p1.rect)
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
        
    pygame.display.update()

    timer.tick(60)

#ending pygame
pygame.quit()
    
    
      

