#Kaiyuan Liu (kl669) Syed Nasif Haq (snh46)
#ECE 5990 Lab 1 2/24/2016
#~/bin/bash
python more_video_control_cb.py &
amixer sset PCM,0 100%
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -slave -input file=/home/pi/fifos/video_fifo /home/pi/bigbuckbunny320p.mp4 -ao alsa
