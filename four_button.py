#Kaiyuan Liu(kl669) Syed Nasif Haq(snh46)
#ECE 5990 Lab 1 02/24/2016
import RPi.GPIO as GPIO
import time
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


#monitor input
while(True):
  if not GPIO.input(sw1):
    print("Button 22 has been pressed")
    time.sleep(0.75)
  if not GPIO.input(sw2):
    print("Button 27 has been pressed")
    time.sleep(0.75)
  if not GPIO.input(sw3):
    print("Button 17 has been pressed")
    time.sleep(0.75)
  if not GPIO.input(sw4):
    print("Button 23 has been pressed")
    time.sleep(0.75)


