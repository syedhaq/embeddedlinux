#Kaiyuan Liu (kl669) Syed Nasif Haq (snh46)
#ECE 5990 Lab 1 02/24/2016
from subprocess import call
import os
commands=['play','pause','volup','voldown','quit'] #List of valid commands
quitscript=False #variable to decided wheather to quit the script or not
valid=False 
vol=50

# function to play and pause movie
def play(vol):
  os.system('echo "pause" > /home/pi/fifos/video_fifo')
  return vol
#function to turn the volume up
def volume_up(vol):
  vol=vol+10
  os.system('echo "volume '+str(vol)+' '+str(1)+'\" > /home/pi/fifos/video_fifo')
  return vol
#function to turn the volume down
def volume_down(vol):
  vol=vol-10
  os.system('echo "volume '+str(vol)+' '+str(1)+'\" > /home/pi/fifos/video_fifo')
  return vol
#function to quit the movie
def quit(vol):
  os.system('echo "quit" > /home/pi/fifos/video_fifo')
  return vol

#dictionary to map the commands to the functions
options={"play":play,"pause":play,"quit":quit,"volup":volume_up,"voldown":volume_down} 

#loop that asks the user to enter a command, checks if the command is valid 
#and calls the appropreate function.
#If command is not valid displays invalid command and aks the user for a new command.
#Commands are as follows:
#play: Plays the movie
#pause: pauses the movie
#volup: turns the volume up
#voldown: turns the volume down
#quit: quits the movie
#qs: quits the python script 
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


