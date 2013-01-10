__author__ = 'ober'
#test
import cv2
import time

cv2.namedWindow("Cam")
CAM=cv2.VideoCapture(0)
if CAM==None :
    exit()
CAM.set(3,640)
CAM.set(4,480)
for i in range(1,16):
    print '%s %s' %(i,CAM.get(i))

while(1):
    _,f=CAM.read();
    i=i+1
    print i
    if ((i % 1 )==0):
        cv2.imshow("Cam",f)
        s="image"+str(i)+".jpg"
     #   cv2.imwrite(s,f)
    if(f==None):
        CAM=cv2.VideoCapture(0)
    time.sleep(0.1)
    if cv2.waitKey(1)!= -1 :
        break