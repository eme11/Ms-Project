import os
import time
import datetime
from emai_send import send_mail_attachment

time.sleep(1)
text ="Home security was down. Now it is back up.\nThe survailance started again at: "
date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
text2 = "\n In the attachment you can find the last saved stream\n"
body = text + date + text2

send_mail_attachment("raspberrypi.camera.project@gmail.com", "PassWord12",
              "emese.mathe.07@gmail.com",
              "Allert Back on",body,'/home/pi/Desktop/stream.h264')