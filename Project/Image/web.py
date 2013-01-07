
#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2.cv as cv
from cv import *
import sys
import time
from threading import Thread
#import serial


servoPos=0
# size = cv.Size(640, 480)
hsv_frame = cv.CreateImage((640, 480), cv.IPL_DEPTH_8U, 3)
thresholded = cv.CreateImage((640, 480), cv.IPL_DEPTH_8U, 1)
thresholded2 = cv.CreateImage((640, 480), cv.IPL_DEPTH_8U, 1)

hsv_min = cv.Scalar(0, 50, 170, 0)
hsv_max = cv.Scalar(10, 180, 256, 0)
hsv_min2 = cv.Scalar(170, 50, 170, 0)
hsv_max2 = cv.Scalar(256, 180, 256, 0)

cv.NamedWindow( "Camera", CV_WINDOW_AUTOSIZE );
capture = cv.CreateCameraCapture(0)
while 1:
            # get a frame from the webcam
            frame = cv.QueryFrame(capture)
            if frame is not None:

               # convert to HSV for color matching
                # as hue wraps around, we need to match it in 2 parts and OR together
                cv.CvtColor(frame, hsv_frame, CV_BGR2HSV)
                cv.InRangeS(hsv_frame, hsv_min, hsv_max, thresholded)
                cv.InRangeS(hsv_frame, hsv_min2, hsv_max2, thresholded2)
                cv.Or(thresholded, thresholded2, thresholded)

               # pre-smoothing improves Hough detector
                cv.Smooth(thresholded, thresholded, CV_GAUSSIAN, 9, 9)
                storage = cv.CreateMat(50, 1, cv.CV_32FC3)
                circles = cv.HoughCircles(thresholded, storage, cv.CV_HOUGH_GRADIENT, 2, thresholded.height/4, 100, 40, 20, 200)

               # find largest circle
                maxRadius = 0
                x = 0
                y = 0
                found = False
                print circles
                if circles != None:
                    for i in range(circles.total):
                        circle = circles[0]
                        if circle[2] > maxRadius:
                            found = True
                            maxRadius = circle[2]
                            x = circle[0]
                            y = circle[1]
                cv.ShowImage( "Camera", frame )
                print 'frame'
                if found:
                    print "ball detected at position:",x, ",", y, " with radius:", maxRadius
                    if x > 420:
                        # need to pan right
                        servoPos += 5
                        servoPos = min(140, servoPos)
                       # servo(2, servoPos)
                    elif x < 220:
                        servoPos -= 5
                        servoPos = max(40, servoPos)
                      #  servo(2, servoPos)
                    print "servo position:", servoPos
                else:
                    print "no ball"

            waitKey(2)
