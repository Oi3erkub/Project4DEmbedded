from numpy import zeros
__author__ = 'ober'
import cv
cv.NamedWindow("as",cv.WINDOW_AUTOSIZE)
cv.NamedWindow("2",cv.WINDOW_AUTOSIZE)
cv.NamedWindow("3",cv.WINDOW_AUTOSIZE)
cv.NamedWindow("4",cv.WINDOW_AUTOSIZE)
im = cv.LoadImage("flish2.bmp", cv.CV_LOAD_IMAGE_COLOR)
gray = cv.CreateImage((im.width, im.height), 8, 1)
edge = cv.CreateImage((im.width, im.height), 8, 1)
h_plane = cv.CreateImage((im.width, im.height), 8, 3)
#h_x = cv.CreateImage((im.width, 1), 8, 1)
#h_y = cv.CreateImage((1,im.height),8,1)
h_x= zeros([im.width,1], int)
h_y= zeros([1,im.height], int)
if 1==1 :
    cv.CvtColor(im,gray,cv.CV_BGR2GRAY)
    ims = gray
    src = gray
    dest = cv.CreateMat(src.height, src.width, cv.CV_16S)
    cv.Sobel(src, dest, 1, 1)

    font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)
 # cv.PutText(im,"Hello World", (5,20),font, 100)

    cv.Zero(h_x)
    cv.Zero(h_y)
    cv.Zero(h_plane)
    for y in range(0, ims.height):
        for x in range(0, ims.width):
            a=cv.Get2D(ims, y, x)
            #ax=cv.Get2D(h_x, 0, x)
           # ay=cv.Get2D(h_y, y, 0)# Slow get pixel value.
            if(a[0] < 100):
               # print a[0]
                cv.Set2D(ims, y, x, (0, 0, 0, 0)) # Slow set pixel value.
            elif (a[0]>220):
                cv.Set2D(ims, y, x, (0, 0, 0, 0)) # Slow set pixel value.
            #cv.Set2D(h_x,0,x,(a[0]+ax[0],0,0,0))
            #cv.Set2D(h_y,y,0,(a[0]+ay[0],0,0,0))
            a=cv.Get2D(ims, y, x)
            if a[0]>150:
             h_x[x,0]+=1
             h_y[0,y]+=1
        #print h_y[0]

    for y in range(0, ims.height):
        cv.Set2D(h_plane, y,h_y[0,y], (255, 255, 255, 255))
    for x in range(0, ims.width):
        cv.Set2D(h_plane, h_x[x,0],x, (255, 255, 255, 255))
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
            if(h_y[0,y]>10):
                y1=y
                cky+=1
        elif(cky==1):
            if(h_y[0,y]>max):
                max=h_y[0,y]
    cky=0
    for y in range( ims.height-1,0,-1):
        if(cky==0):
            if(h_y[0,y]>10):
                y4=y
                cky+=1
        elif(cky==1):
            if(h_y[0,y]>max):
                max=h_y[0,y]

    cv.Line(im,(0,y1),(500,y1),(255,255,0),thickness=3)
    cv.Line(im,(x1,0),(x1,500),(255,255,0),thickness=3)
    cv.Line(im,(0,y4),(500,y4),(255,255,0),thickness=3)
    cv.Line(im,(x4,0),(x4,500),(255,255,0),thickness=3)
    cv.ShowImage("as",im)
    cv.ShowImage("2",ims)
    cv.ShowImage("3",h_plane)
    cv.ShowImage("4",dest)
while 1:
    c=cv.WaitKey(1000)
    if c== 27 :
            break