from pickle import TRUE
from turtle import circle, window_height
import pygame
import time

# screen size 
WINDOW_W = 1000
WINDOW_H = 524
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

# music defenition
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.set_volume(0.0  )
pygame.mixer.music.play()
pygame.mixer.music.load("gunshot.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load("explosion.mp3")
pygame.mixer.music.set_volume(7.0)
pygame.mixer.Channel(1).play(pygame.mixer.Sound('song.mp3'))

# text_color = (68,132,88)
# myfont = pygame.FONT.skyfont("comicsans",30)
# textsurfase=myfont.render('score:',True,(255,255,255))

score1=0
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS",30)
textsurfase=myfont.render('score:',True,(255,255,255))
font=pygame.font.SysFont("fhir",30,50)
score=font.render(str(score1),False,(255,255,255))


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("star wars")
bk_image = pygame.image.load("background.jpg")
ship_image=pygame.image.load("space ship.png")
laser_image=pygame.image.load("pngaaa.com-25809.png")
ship_image=pygame.transform.scale(ship_image,(50,80))
laser_image=pygame.transform.scale(laser_image,(30,40))

clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H /2
x_step = 10
play = True
ship_x=WINDOW_W/2-25
ship_y=WINDOW_H-80
lasers_beam=[]

def laser_hit(laser):
  return abs(laser[0]-circle_x)<20 and abs(laser[1]-circle_y)<20 



def laserbeam():
  # pygame.draw.line(screen,(255,255,255),(0,1),(1000,1))
  # pygame.draw.line(screen,(255,255,255),(0,2),(1000,2))
  # pygame.draw.line(screen,(255,255,255),(0,3),(1000,3))
  # pygame.draw.line(screen,(255,255,255),(0,4),(1000,4))
  # pygame.draw.line(screen,(255,255,255),(0,5),(1000,5))
  # pygame.draw.line(screen,(255,255,255),(0,6),(1000,6)) 
  for i in range(len(lasers_beam)-1,0,-1):
    global score1
    global circle_x 
    lb=lasers_beam[i]
    screen.blit(laser_image,(lb[0],lb[1]))
    lasers_beam[i]=[lb[0],lb[1]-5]
    if laser_hit(lb):
      score1+=1
      pygame.mixer.Channel(3).play(pygame.mixer.Sound('explosion.mp3'))
      circle_x=0
      lasers_beam.pop(i)
      
   
      



while play:
  # screen.fill(BK_COLOR)
  screen.blit(textsurfase,(10,20))
  screen.blit(bk_image,(0,0)) 
  screen.blit(ship_image,(ship_x,ship_y))
  pygame.draw.circle(screen,(255,255,255),(circle_x , circle_y),10)
  screen.blit(textsurfase,(10,5))
  score=font.render(str(score1),False,(255,255,255)) 
  screen.blit(score,(100,20))
  circle_x +=x_step
  if circle_x > WINDOW_W:
    x_step = -10
  if circle_x <0 :
    x_step = 10
  laser_x=ship_x+9
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    elif event.type==pygame.KEYDOWN:
      if event.key==pygame.K_LEFT:
        ship_x-=10
      if event.key==pygame.K_RIGHT:
        ship_x+=10
      if event.key==pygame.K_SPACE:
        lasers_beam.append([laser_x,ship_y])
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('gunshot.mp3'))
        
  laserbeam()
        
   
  pygame.display.flip()

  clock.tick(50)

pygame.quit()
