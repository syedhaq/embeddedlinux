from subprocess import call
import os
#import string
commands=['play','pause','volup','voldown','quit']
quitscript=False
valid=False
vol=50

def play(vol):
  os.system('echo "pause" > /home/pi/fifos/video_fifo')
  return vol
def volume_up(vol):
  vol=vol+10
  os.system('echo "volume '+str(vol)+' '+str(1)+'\" > /home/pi/fifos/video_fifo')
  return vol
def volume_down(vol):
  vol=vol-10
  os.system('echo "volume '+str(vol)+' '+str(1)+'\" > /home/pi/fifos/video_fifo')
  return vol
def quit(vol):
  os.system('echo "quit" > /home/pi/fifos/video_fifo')
  return vol
options={"play":play,"pause":play,"quit":quit,"volup":volume_up,"voldown":volume_down}
print(quitscript)
while(quitscript==False):
  print("In while")
  prompt_text = "Enter a command for mplayer: "
  user_in=input(prompt_text)

  if user_in=='qs':
    quitscript=True
  else:
    for i in range(0,len(commands)):
      if user_in==commands[i]:
        valid=True
        break

    if valid:
      vol=options[user_in](vol)
      valid=False  

    else:
      print ("invalid command")


