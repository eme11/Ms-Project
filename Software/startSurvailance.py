#using os.system we execute some shell commands
import os
os.system('sudo python notifyMotionDetection.py |raspivid -o - -t 0 -vf -hf -fps 60 -b 500000 |tee stream.h264| ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/68km-m5y1-hrd2-76za ' )