import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

#DEFINE COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#ASSET FOLDERS
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#PLAYER CLASS
class Player(pygame.sprite.Sprite):
              def __init__(self): 
                            pygame.sprite.Sprite.__init__(self)
                            self.image = pygame.image.load("p1_jump.png").convert()
                            self.image.set_colorkey(BLACK)
                            self.rect = self.image.get_rect()
                            self.rect.center = (WIDTH / 2, HEIGHT / 2)
                            self.y_speed = 5
              def update(self):


                            #RETURNS A LIST, keystate, OF ALL PRESSED KEYS
                            keystate = pygame.key.get_pressed()

                            #CHECK TO SEE WHICH KEY WERE IN THE LIST (A.K.A. PRESSED
                            if keystate[pygame.k_RIGHT]:
                                          self.rect.x += 5
                            if keystate[pygame.k_LEFT]:
                                          self.rect.x += 5
                            if keystate[pygame.k_RIGHT]:
                                          self.rect.x += -5
                            if keystate[pygame.k_LEFT]:
                                          self.rect.x += -5

#INITIALIZE VARIABLES
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

#SPRITE GROUPS
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#GAME LOOP:
#  Process Events
#  Update
#  Draw
running = True
while running:

              clock.tick(FPS)

              #PROCESS EVENTS
              for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                          running = False
                            

              #UPDATE
              all_sprites.update()

              #  DRAW
              screen.fill(BLUE)
              all_sprites.draw(screen)

              #  FLIP AFTER DRAWING
              pygame.display.flip()

pygame.quit

























