__author__ = 'ober'
from numpy import zeros
import cv

cv.NamedWindow("as",cv.WINDOW_AUTOSIZE)
im = cv.LoadImage("flish2.bmp", cv.CV_LOAD_IMAGE_COLOR)
cv.Smooth(im,im, cv.CV_GAUSSIAN, 3, 15)
gray = cv.CreateImage((im.width, im.height), 8, 1)
edge = cv.CreateImage((im.width, im.height), 8, 1)
h_plane = cv.CreateImage((im.width, im.height), 8, 3)
h_plane2 = cv.CreateImage((im.width, im.height), 8, 3)
cv.CvtColor(im,gray,cv.CV_BGR2GRAY)
cv.CvtColor(im,h_plane,cv.CV_BGR2HSV)

thresholded_img =  cv.CreateImage(cv.GetSize(h_plane), 8, 1)

#   while cv.WaitKey(1000)!=27:
cv.InRangeS(h_plane, (111, 0, 0), (255, 255, 255), thresholded_img)
cv.ShowImage("as",thresholded_img)

h_x= zeros([im.width,1], int)
h_y= zeros([1,im.height], int)
if 1==1 :
    cv.CvtColor(im,gray,cv.CV_BGR2GRAY)
    ims = thresholded_img
    font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)
    cv.PutText(im,"Hello World", (150,50),font, 255)

    cv.Zero(h_x)
    cv.Zero(h_y)
    cv.Zero(h_plane)
    cv.Zero(h_plane2)
    for y in range(0, ims.height):
        for x in range(0, ims.width):
            a=cv.Get2D(ims, y, x)

            if a[0]>150:
                h_x[x,0]+=1
                h_y[0,y]+=1
                #print h_y[0]

    for y in range(0, ims.height):
        cv.Set2D(h_plane, y,h_y[0,y], (255, 255, 0, 0))
        cv.Line(h_plane, (h_y[0,y],y), (0,y), cv.Scalar(0,255,0), 1)
    for x in range(0, ims.width):
        cv.Set2D(h_plane2, h_x[x,0],x, (255, 0, 255, 0))
        cv.Line(h_plane2, (x,0), (x,h_x[x,0]), cv.Scalar(255,0,0), 1)


    chx=0
    x1=0
    x2=0
    x3=0
    x4=0
    ckx=0
    max=0
    min=9999

    for x in range(0, ims.width):
        if(ckx==0):
            if(h_x[x,0]>10):
                x1=x
                ckx+=1
        elif(ckx==1):
            if(h_x[x,0]>max):
                max=h_x[x,0]
    ckx=0

    for x in range(ims.width-1,0,-1):
        print x
        if(ckx==0):
            if(h_x[x,0]>10):
                x4=x
                ckx+=1
        elif(ckx==1):
            if(h_x[x,0]>max):
                max=h_x[x,0]






    y1=0
    y2=0
    y3=0
    y4=0
    cky=0
    for y in range(0, ims.height):
        if(cky==0):
            if(h_y[0,y]>20):
                y1=y
                cky+=1
        elif(cky==1):
            if(h_y[0,y]>max):
                max=h_y[0,y]
    cky=0
    for y in range( ims.height-1,0,-1):
        if(cky==0):
            if(h_y[0,y]>20):
                y4=y
                cky+=1
        elif(cky==1):
            if(h_y[0,y]>max):
                max=h_y[0,y]

    cv.Line(im,(0,y1),(ims.width,y1),(0,255,0),thickness=3)
    cv.Line(im,(x1,0),(x1,ims.height),(255,0,0),thickness=3)
    cv.Line(im,(0,y4),(ims.width,y4),(0,255,0),thickness=3)
    cv.Line(im,(x4,0),(x4,ims.height),(255,0,0),thickness=3)


    cv.ShowImage("as",im)
    cv.ShowImage("2",ims)

    edges = cv.CreateImage(cv.GetSize(im), 8, 1)
    edges2 = cv.CreateImage(cv.GetSize(im), 8, 1)
    gray = cv.CreateImage(cv.GetSize(im), 8, 1)
    #cv.Smooth(ims, ims, cv.CV_BLUR, 15, 15)

    dstSobel = cv.CreateMat(im.height, im.width, cv.CV_32FC1)
   # cv.CvtColor(im, gray, cv.CV_BGR2GRAY)
    #cv.Canny(gray,edges,5,100,3)
    #gary=ims
    #cv.Canny(gray, edges, 50, 200, 3)
    cv.sobel(ims,dstSobel,1,1,1)
    #cv.ShowImage("2",gray)
    cv.ShowImage("3",h_plane)
    cv.ShowImage("4",h_plane2)
    cv.ShowImage("5",dstSobel)

cv.WaitKey(0)
