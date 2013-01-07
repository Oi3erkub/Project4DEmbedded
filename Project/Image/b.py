from numpy import zeros

__author__ = 'ober'
import cv
cv.NamedWindow("as",cv.WINDOW_AUTOSIZE)
cv.NamedWindow("2",cv.WINDOW_AUTOSIZE)
cv.NamedWindow("3",cv.WINDOW_AUTOSIZE)

im = cv.LoadImage("flish.bmp", cv.CV_LOAD_IMAGE_COLOR)
size = (im.width, im.height)
gray = cv.CreateImage((im.width, im.height), 8, 1)
edge = cv.CreateImage((im.width, im.height), 8, 1)
h_plane = cv.CreateImage((im.width, im.height), 8, 3)

hsv_frame = cv.CreateImage(size,cv.IPL_DEPTH_8U, 3)
thresholded = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
thresholded2 = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
hsv_min = cv.Scalar(300, 50, 170, 0)
hsv_max = cv.Scalar(360, 180, 256, 0)
hsv_min2 = cv.Scalar(170, 50, 170, 0)
hsv_max2 = cv.Scalar(256, 180, 256, 0)

cv.CvtColor(im, hsv_frame, cv.CV_BGR2HSV)
cv.InRangeS(hsv_frame, hsv_min, hsv_max, thresholded)
#cv.InRangeS(hsv_frame, hsv_min2, hsv_max2, thresholded2)
#cv.Or(thresholded, thresholded2, thresholded)
#h_x = cv.CreateImage((im.width, 1), 8, 1)
#h_y = cv.CreateImage((1,im.height),8,1)
h_x= zeros([im.width,1], int)
h_y= zeros([1,im.height], int)
if 1==1 :
    cv.CvtColor(im,gray,cv.CV_BGR2GRAY)
    ims = gray
    font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)
    cv.PutText(im,"Hello World", (5,20),font, 255)

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
        cv.Set2D(h_plane, y,h_y[0,y], (255, 255, 0, 0))
    for x in range(0, ims.width):
        cv.Set2D(h_plane, h_x[x,0],x, (255, 0, 255, 0))
    cv.ShowImage("as",im)
    cv.ShowImage("2",ims)
    cv.ShowImage("3",h_plane)
 #   cv.ShowImage( "2", gray );
while 1:
    c=cv.WaitKey(1000)
    if c== 27 :
        break