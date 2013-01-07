__author__ = 'ober'
import cv
cv.NamedWindow("3",cv.WINDOW_AUTOSIZE)
c=cv.CaptureFromCAM(0)
cv.SetCaptureProperty( c, cv.CV_CAP_PROP_FRAME_WIDTH, 1024 )
i=0;
while True:


    f=cv.QueryFrame(c)
    gray = cv.CreateImage((f.width, f.height), 8, 1)
    cv.CvtColor(f,gray,cv.CV_BGR2GRAY)

    cv.ShowImage("3",f)
    c1=cv.WaitKey(1)
    if (c1== 27):
        break
    elif(c1 !=-1):
       
        cv.SaveImage("asd",f)