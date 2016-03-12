
import RPi.GPIO as GPIO
import time
from subprocess import call
import os
#switch definitions
sw1=22
sw2=27
sw3=17
sw4=23

#Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#Loop Exit setup
quitscript=False
valid=False
vol=50

#mplayer function definitions
def play():
  os.system('echo "pause" > /home/pi/fifos/video_fifo')
def rewind():
  os.system('echo "seek -10" > /home/pi/fifos/video_fifo')
def fast_forward():
  os.system('echo "seek 10" > /home/pi/fifos/video_fifo')
def quit():
  os.system('echo "quit" > /home/pi/fifos/video_fifo')

#monitor input that asks user to press buttons
while(not quitscript):
    if not GPIO.input(sw1):
      print("Play Button")
      play()
      time.sleep(0.75)
    if not GPIO.input(sw2):
      print("Stop Button")
      quit()
      time.sleep(0.75)
    if not GPIO.input(sw3):
      print("Fast forwad button")
      fast_forward()
      time.sleep(0.75)
    if not GPIO.input(sw4):
      print("Rewind button")
      rewind()
      time.sleep(0.75)

