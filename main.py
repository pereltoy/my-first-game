from turtle import circle
import pygame
import time

# screen size 
WINDOW_W = 1000
WINDOW_H = 524
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

# BK_COLOR = (68,132,88)

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


def laserbeam():
  pygame.draw.line(screen,(255,255,255),(0,1),(1000,1))
  pygame.draw.line(screen,(255,255,255),(0,2),(1000,2))
  pygame.draw.line(screen,(255,255,255),(0,3),(1000,3))
  pygame.draw.line(screen,(255,255,255),(0,4),(1000,4))
  pygame.draw.line(screen,(255,255,255),(0,5),(1000,5))
  pygame.draw.line(screen,(255,255,255),(0,6),(1000,6))
  for i in range(len(lasers_beam)):
    lb=lasers_beam[i]
    screen.blit(laser_image,(lb[0],lb[1]))
    lasers_beam[i]=[lb[0],lb[1]-10]
    if lb[1]<1  :
      lasers_beam.remove(lasers_beam[i])

while play:
  # screen.fill(BK_COLOR)
  screen.blit(bk_image,(0,0)) 
  screen.blit(ship_image,(ship_x,ship_y))
  pygame.draw.circle(screen,(255,255,255),(circle_x , circle_y),10)
  
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
        laserbeam()
        
  laserbeam() 
  pygame.display.flip()

  clock.tick(50)

pygame.quit()
