
import RPi.GPIO as GPIO
import time
from subprocess import call
import os
#switch definitions
sw1=22
sw2=27
sw3=17
sw4=23
sw5=6
sw6=12

#Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw5,GPIO.IN)
GPIO.setup(sw6,GPIO.IN)
#Loop Exit setup

vol=50

#mplayer function definitions
def play(channel):
  os.system('echo "pause" > /home/pi/fifos/video_fifo')
def rewind(channel):
  os.system('echo "seek -10" > /home/pi/fifos/video_fifo')
def fast_forward(channel):
  os.system('echo "seek 10" > /home/pi/fifos/video_fifo')
def rewind30(channel):
  os.system('echo "seek -30" > /home/pi/fifos/video_fifo')
def fast_forward30(channel):
  os.system('echo "seek 30" > /home/pi/fifos/video_fifo')
def quit(channel):
  os.system('echo "quit" > /home/pi/fifos/video_fifo')

#monitor input that asks user to press buttons
GPIO.add_event_detect(sw1,GPIO.FALLING,callback=play,bouncetime=300)
GPIO.add_event_detect(sw3,GPIO.FALLING,callback=fast_forward,bouncetime=300)
GPIO.add_event_detect(sw4,GPIO.FALLING,callback=rewind,bouncetime=300)
GPIO.add_event_detect(sw5,GPIO.FALLING,callback=fast_forward30,bouncetime=300)
GPIO.add_event_detect(sw6,GPIO.FALLING,callback=rewind30,bouncetime=300)
GPIO.add_event_detect(sw2,GPIO.FALLING,callback=quit,bouncetime=300)
beginTime=time.time()
timeElapsed=0;
while timeElapsed<=5:
  try:
   # time.sleep(0.00002)
    timeElapsed=time.time()-beginTime
    pass
  except KeyboardInterrupt:
    GPIO.cleanup() 
