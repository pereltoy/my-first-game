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
pygame.display.set_caption("star wars ")

bk_image = pygame.image.load("background.jpg")
ship_image=pygame.image.load("space ship.png")
ship_image=pygame.transform.scale(ship_image,(50,80))

clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H /2
x_step = 10
play = True
ship_x=WINDOW_W/2-25
ship_y=WINDOW_H-80
fire_blast=ship_y-50
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
  
  
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    elif event.type==pygame.KEYDOWN:
      if event.key==pygame.K_LEFT:
        ship_x-=10
      if event.key==pygame.K_RIGHT:
        ship_x+=10
      if event.key==pygame.K_BACKSPACE:
        pygame.draw.circle(screen,(255,255,255),(ship_x , fire_blast),10)
        fire_blast-=5



  clock.tick(50)

pygame.quit()
