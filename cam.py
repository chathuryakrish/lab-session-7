import os
i=0
while(i<=10):
    os.system("fswebcam -F 4 --fps 30 -r 1200*1000 /home/pi/group2/"+str(i)+".jpg")
    i=i+1
