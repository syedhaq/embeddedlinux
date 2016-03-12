import sys,pygame,time
import os

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

class Balls:
 def __init__(self,image,speed,pos):
  self.speed=speed
  self.image=image
  self.pos=image.get_rect().move(pos,0)
 def move(self,size):
   self.pos=self.pos.move(self.speed)
   if self.pos.left<0 or self.pos.right>width:
     self.speed[0]=-self.speed[0]
   if self.pos.top<0 or self.pos.bottom>height:
     self.speed[1]=-self.speed[1]
 def collide(self):
   self.speed[0]=-self.speed[0]
   self.speed[1]=-self.speed[1]
    


pygame.init()

size=width,height=320,240
speed0=[1,1]
speed1=[3,3]
black=0,0,0

screen=pygame.display.set_mode(size)
ballsm=pygame.image.load("magic_ball.png")
balll=pygame.image.load("magic_ball_big.png")

ball0=Balls(ballsm,speed0,0)
ball1=Balls(balll,speed1,200)
objects=[ball0,ball1]

while 1:
  for event in pygame.event.get():
    if (event.type is MOUSEBUTTONDOWN):sys.exit()

  for o in objects:
    screen.fill(black)
 

  ball0.move(size)
  screen.blit(ball0.image,ball0.pos)
  ball1.move(size)
  screen.blit(ball1.image,ball1.pos)

  
  #Check for collision
  if ball0.pos.colliderect(ball1.pos):
    ball0.collide()
    ball1.collide()
    
  pygame.display.update()
  pygame.time.delay(10)
