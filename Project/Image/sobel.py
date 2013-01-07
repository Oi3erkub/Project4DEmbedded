__author__ = 'ober'
from numpy import *
import cv
# load and show an image in gray scale
image = cv.LoadImage('flish2.bmp',cv.CV_LOAD_IMAGE_GRAYSCALE)
imageBlur = cv.CreateImage(cv.GetSize(image), image.depth, image.nChannels)


# print some image properties
print 'Depth:',image.depth,'# Channels:',image.nChannels
print 'Size:',image.width,image.height
print 'Pixel values average',cv.Avg(image)

# create the window
cv.NamedWindow('my window', cv.CV_WINDOW_AUTOSIZE)

dstSobel = cv.CreateMat(image.height, image.width, cv.CV_32FC1)
cv.Smooth(image, imageBlur, cv.CV_BLUR, 15, 15)
cv.Sobel(imageBlur,dstSobel,1,1,5)
cv.ShowImage('my sobal', dstSobel)
#cv.Canny(imageBlur,dstSobel,50,100,3)
cv.ShowImage('my window', imageBlur)
#cv.ShowImage('sobel', dstSobel)
cv.WaitKey()
cv.SaveImage('imageSobel.jpg', dstSobel)

cv.waitKey(0);