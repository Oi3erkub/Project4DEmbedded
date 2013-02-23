__author__ = 'ober'

import threading
import time
import cv2
import serial
import socket
import Queue

exitFlag = 0
Sacal = 0

class Cam (threading.Thread):
    def __init__(self, threadID, name):
        self.threadID = threadID
     #   self.name = name
      #  self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        print "Starting CAM " + self.name
        cv2.namedWindow("Cam")
        CAM=cv2.VideoCapture(0)
        if CAM==None :
            exit()
        CAM.set(3,640)
        CAM.set(4,480)
        for i in range(1,16):
            print '%s %s' %(i,CAM.get(i))

        while(not exitFlag):

            if not KgQueue.empty():
                queueLock.acquire()
                Kg=KgQueue.get()
                UIQueue.put(Kg)
                UIQueue.put(Kg)
                print "Scale "+ Kg
                _,f=CAM.read()
                _,f=CAM.read()
                i=i+1
                print i
                cv2.imshow("Cam",f)
                s="image"+str(i)+Kg+".jpg"
                cv2.imwrite(s,f)
                if(f==None):
                    CAM=cv2.VideoCapture(0)
                time.sleep(0.5)
                if cv2.waitKey(1)!= -1 :
                    break
                print "cam"
                queueLock.release()

            #time.sleep(0.5)
        print "EXit cam"

class Kg (threading.Thread):
    def __init__(self, threadID, name):
        self.threadID = threadID
        #      self.name = name
#        self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        print "Starting Kg " + self.name
        ser = serial.Serial( port='COM22',  baudrate=9600) # open first serial port
        print ser.portstr
        buff = ""
        while not exitFlag:
            c = ser.read()
            if  c == '+' :
                buff = ""
            elif c != 'k' :
                buff = buff + c
            else:
                print buff
                ia=intern(buff)
                print ia
                queueLock.acquire()
                KgQueue.put(buff)
                queueLock.release()
                print "Kg"
                buff = ""
        print "Exit Kg"



class Rfid (threading.Thread):
    def __init__(self, threadID, name):
        self.threadID = threadID
        #      self.name = name
        #        self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        print "Starting Rfid " + self.name
        ser = serial.Serial( port='COM23',  baudrate=115200) # open first serial port
        print ser.portstr
        buff = ""
        while not exitFlag:
            c = ser.read()
            if  c == '+' :
                buff = ""
            elif c != 'k' :
                buff = buff + c
            else:
                print buff
                ia=intern(buff)
                print ia
                queueLock.acquire()
                RfQueue.put(buff)
                queueLock.release()
                print "RF"
                buff = ""
        print "Exit RF"
class UI (threading.Thread):
    def __init__(self, threadID, name):
        self.threadID = threadID
        #      self.name = name
        #        self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        print "Starting UI " + self.name

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while not exitFlag:
            try:
                client_socket.connect(('192.168.42.129',6000))
                print "Connect"
                break
            except:
                print "Not connect"
                time.sleep(5)


        while not exitFlag:
            #data=client_socket.recv(16)
           # data = raw_input ( "SEND( TYPE q or Q to Quit):" )
            if not UIQueue.empty():
                queueLock.acquire()

                dataKg=UIQueue.get()
                dataRFID=UIQueue.get()
                print "UI"+dataKg
                data=dataKg+'\n'
                client_socket.send(data)

                queueLock.release()

#------------------------------------------------------------------------------------------------------
# Create Queue
queueLock = threading.Lock()
KgQueue = Queue.Queue(10)
RfQueue = Queue.Queue(10)
UIQueue = Queue.Queue(10)
# Create new threads
thread1 = Cam(1, "Thread-Cam")
thread2 = Kg(2,"Thread-Kg")
thread3 = Rfid(3,"Thread-Rfid")
thread4 = UI(4,"Thread-Rfid")
# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

while thread1.isAlive():
    if not thread1.isAlive():
        exitFlag = 1
    pass
print "Exiting Main Thread"