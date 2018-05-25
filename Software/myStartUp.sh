#this scipt is located in the /etc/profile.d/myStartUp.sh 
#this is will launch the script automatically after login
cd /
cd /home/pi/Desktop
sudo python notifyStartUp.py
sudo python startSurvailance.py
cd /
