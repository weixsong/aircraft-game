import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
  pygame.init()
  screen = pygame.display.set_mode((468, 60))
  pygame.display.set_caption('Monkey Fever')
  pygame.mouse.set_visible(0)

  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((250, 250, 250))


  if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)

  screen.blit(background, (0, 0))
  pygame.display.flip()

#Prepare Game Objects
  clock = pygame.time.Clock()
  chimp = Chimp()
  fist = Fist()
  allsprites = pygame.sprite.RenderPlain((fist, chimp))

  while 1:
    clock.tick(60)

    #Handle Input Events
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN and event.key == K_ESCAPE:
        return
      elif event.type == MOUSEBUTTONDOWN:
        if fist.punch(chimp):
          punch_sound.play() #punch
          chimp.punched()
        else:
          whiff_sound.play() #miss
      elif event.type is MOUSEBUTTONUP:
        fist.unpunch()

    allsprites.update()
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()

if __name__ == '__main__':
  main()