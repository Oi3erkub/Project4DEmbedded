__author__ = 'ober'
import cv
dims=(9,6)
c=cv.CaptureFromCAM(0)
c2=cv.CaptureFromCAM(0)
while True:
    f=cv.QueryFrame(c)
    f2=cv.QueryFrame(c2)
    grey = cv.CreateImage((f.width, f.height), 8, 1)
    grey2 = cv.CreateImage((f.width, f.height), 8, 1)
    cv.CvtColor(f,grey,cv.CV_BGR2GRAY)
    cv.CvtColor(f2,grey2,cv.CV_BGR2GRAY)
    found,points=cv.FindChessboardCorners(grey,dims,cv.CV_CALIB_CB_ADAPTIVE_THRESH)
    found2,points2=cv.FindChessboardCorners(grey2,dims,cv.CV_CALIB_CB_ADAPTIVE_THRESH)
    if found!=0:
        cv.DrawChessboardCorners(f,dims,points,found)
    if found2!=0:
        cv.DrawChessboardCorners(f2,dims,points2,found2)
    cv.ShowImage("winL",f)
    cv.ShowImage("winR",f2)
    k=cv.WaitKey(2)
    if k == 27 :
        break
    print(k);
