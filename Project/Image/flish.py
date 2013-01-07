__author__ = 'ober'
import cv
g_switch_value =0
g_switch_value2 =0
lo =120
lo2 =120

def onTrackbarSlide(pos):
   global lo
   lo = pos

   cv.InRangeS(h_plane, (lo, 0, 0), (lo2, 255, 255), thresholded_img)
   cv.ShowImage("as",thresholded_img)
   print lo ,lo2

def onTrackbarSlide2(pos):
    global lo2
    lo2 = pos
    cv.InRangeS(h_plane, (lo, 0, 0), (lo2, 255, 255), thresholded_img)
    cv.ShowImage("as",thresholded_img)
    print lo ,lo2
if __name__ == '__main__':
    cv.NamedWindow("as",cv.WINDOW_AUTOSIZE)
    im = cv.LoadImage("flish2.bmp", cv.CV_LOAD_IMAGE_COLOR)
    cv.Smooth(im,im, cv.CV_GAUSSIAN, 3, 3)
    gray = cv.CreateImage((im.width, im.height), 8, 1)
    edge = cv.CreateImage((im.width, im.height), 8, 1)
    h_plane = cv.CreateImage((im.width, im.height), 8, 3)

    cv.CvtColor(im,gray,cv.CV_BGR2GRAY)
    cv.CvtColor(im,h_plane,cv.CV_BGR2HSV)

    thresholded_img =  cv.CreateImage(cv.GetSize(h_plane), 8, 1)

 #   while cv.WaitKey(1000)!=27:
    cv.InRangeS(h_plane, (lo, 0, 0), (lo2, 255, 255), thresholded_img)
    cv.ShowImage("as",thresholded_img)
    cv.CreateTrackbar( "Switch", "as", 1, 255, onTrackbarSlide)
    cv.CreateTrackbar( "Switch2", "as", 1, 255, onTrackbarSlide2)
    print lo , g_switch_value
    print lo , g_switch_value
   # onTrackbarSlide(0)
    cv.WaitKey(0)

