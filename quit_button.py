import pygame, sys, time
from pygame.locals import *
import os


#Colours
WHITE = (255,255,255)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None, 50)

touch_buttons = {'Quit':(280,220)}

for k,v in touch_buttons.items():
    text_surface = font_big.render('%s'%k, True, WHITE)
    rect = text_surface.get_rect(center=v)
    lcd.blit(text_surface, rect)

pygame.display.update()
begin_time=time.time()
running=True
while running:
    elapsed=time.time()-begin_time
    if elapsed>100000:
        running=False
    # Scan touchscreen events
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            print(pos)
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            print(pos)
            #Find which quarter of the screen we're in
            x,y = pos
            if y > 200:
                if x > 270:
                  sys.exit()                    
    time.sleep(0.1)
