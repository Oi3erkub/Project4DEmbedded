#ras
import threading
import time
import socket
import Queue
import sys


import sqlite3

datams = ""
class BackMS(threading.Thread):
    def __init__(self, threadID, c):
        self.threadID = threadID
        self.c = c
        #        self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        a=""
        while(a!="BACKMS"):
            a=rl(c)
            global datams
            datams=a
        print "out backms"
        wl(c,"exit")


def wl(socket1,data):
    data=data+"\n"
    socket1.sendall(data)
def rl(socket1):
    c=""
    a=""
    while((c)!= "\n"):
        c= socket1.recv(1)
        print c
        if c=="":
            break
        if c!="\n":
            a=a+c
    return a
def sendlist(socket,data,count):
    print "count " + count
    wl(socket,count)
    print "send " + count
    for row in data:
        wl(socket,str(row[0]))
        print row[0]

def revlist((socket)):
    count=int(rl(socket))
    for i in  range(1,count):
        print rl(socket)






def insertFA(db, data):
    db.execute("insert into fname(name) values (?)", (data,))
def createTB(db):
    db.execute('''create table fname (ID INTEGER PRIMARY KEY,name TEXT UNIQUE NOT NULL)''')
def selectFA(db):
    row=db.execute("select name from fname")
    return row
def selectcountFA(db):
    row=db.execute("select count(*) from fname")
    data=row.fetchone()[0]
    return str(data)
    #Insert a row of data



conn = sqlite3.connect('example.db')
db = conn.cursor()
try:
    print "Tabal have never Create"
    createTB(db)
except:
    print "Tabal have been Create"
exitFlag = 0

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while(1):
    try:
        c.connect(('192.168.42.129', 6000 ))
        break
     #   c.connect(('127.0.0.1', 6000 ))
    except:
        print "Connect no"

print "Connect"
while not exitFlag:
  input=rl(c)
  print input
  if input!= "":
    if(input=="FA"):
        data=rl(c)
        print "insert " +data
        try:
            insertFA(db,data)
            wl(c,"ok")
            conn.commit()

        except:
            print data +"not unique"
            wl(c,"no")

    if(input=="LF"):
        print "selectFA "
        count=selectcountFA(db)
        data=selectFA(db)
        sendlist(c,data,count)
        print "e"
    if(input=="Bind"):
        wl(c,"ok")
    if(input=="MS"):
        family=rl(c)

        global datams

        threadBack = BackMS(4,c)
        threadBack.start()
        datams=""
        while(datams!="BACKMS"):

            wl(c,"KG")
            wl(c,"2.23456")
            time.sleep(1)
            wl(c,"RF")
            wl(c,"#A 999 274869001429")
            time.sleep(1)
            wl(c,"IMAGE")
            fp=open("flish.bmp","rb")
            imagedata=fp.read()
            wl(c,str(len(imagedata)))
            c.sendall(imagedata)
            print rl(c)

        print "out while ms"





  else:
      conn.commit()
      db.close()
      conn.close()
      c.close()
      print "exit"
      exit()

      time.sleep(0.1)
#  if(input=='AF'):
#    print input
 #   input=c.recv(100)
 #   print 'add '+input+' in DB'

  #sleep(0.1)
#thread4 = test(4,"Thread-ui")
# Start new Threads

#thread4.start()

#while thread4.isAlive():
#    if not thread4.isAlive():
     #   exitFlag = 1
 #       pass
#print "Exiting Main Thread"


