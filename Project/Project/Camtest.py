__author__ = 'ober'

class Camera(threading.Thread):
    def __init__(self,no,x,y):
        self.x=x
        self.y=y
        print "Start Camera"
        #cv2.namedWindow("Cam")
        CAM=cv2.VideoCapture(no)
        if CAM==None :
            print "Camera Error"
            return -1
        CAM.set(3,x)
        CAM.set(4,y)
        threading.Thread.__init__(self)

    def readImage(self):
        CAM.read()#Clear buffer
        _,self.f=CAM.read()

        if(f==None):
            CAM=cv2.VideoCapture(no)

    def SaveImage(self,name):
        cv2.imwrite(name,self.f)
    def run(self):
        print "Starting Cam "
        global ex_threadflag
        while(not ex_threadflag):
        # if (not KgQueue.empty()):# and (not RfQueue.empty()):
        # queueLock.acquire()
        # Kg=KgQueue.get()
        #     Rf=RfQueue.get()
            global ck
            if(ck==1):
                self.readImage()
                self.SaveImage("1.jpg")
                print 'save image'
                global ck
                ck=0
                #RfQueue.queue.clear()
                #KgQueue.queue.clear()
                # queueLock.release()
