__author__ = 'ober'
import threading
import time
import socket
import Queue

exitFlag = 0
def wl(socket1,data):
    data=data+"\n"
    socket1.sendall(data)
def rl(socket1):
    c=""
    a=""
    while((c)!= "\n"):
        c= socket1.recv(1)
        if c=="":
            break
        if c!="\n":
            a=a+c
    return a

def revlist((socket)):
    n=rl(socket)
    print "conut "+ n
    count=int(n)
    for i in  range(0,count):
        print rl(socket)

class ee(threading.Thread):

    def __init__(self, threadID, name):
        self.threadID = threadID
        #      self.name = name
        #        self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        print "Starting 9 "

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 6000))
        print 'bind'
        server.listen(1)
        (s,a)=server.accept()
        print 'accept'

        i=0

        wl(s,"FA")
        wl(s,"name")
        print rl(s)
        wl(s,"FA")
        wl(s,"name2")
        print rl(s)

        wl(s,"LF")
        revlist(s)



        print 's'

        print 'end'
        time.sleep(5)




thread2 = ee (2,"Thread-9")
# Start new Threads

thread2.start()

while thread2.isAlive():
    if not thread2.isAlive():
        exitFlag = 1

        pass
print "Exiting Main Thread"
