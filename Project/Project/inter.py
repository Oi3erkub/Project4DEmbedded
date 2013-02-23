#ras
__author__ = 'ober'
__author__ = 'ober'

import threading
import time
import cv2
import serial
import socket
import Queue
import sqlite3

ex_threadflag=1
DeviceID="1234"
ck=0
FarmID =""
class BackMS(threading.Thread):
    def __init__(self):
        global  ex_threadflag
        ex_threadflag=0
        #        self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        global  ex_threadflag
        a=""
        while(a!="BACKMS"):
            a=Nw.rl()
            global datams
            datams=a
        ex_threadflag=1
        print "out backms"
        Nw.wl("exit")

class Network:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self.c = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while(1):
            try:
                self.sock.connect((ip,port ))
                #   c.connect(('127.0.0.1', 6000 ))
                print "Connect"
                self.c = 1
                break
            except:
                self.c = 0
                print "Connect no"
    def coned(self):
        return  self.c
    def wl(self,data):
        data=data+"\n"
        self.sock.sendall(data)
    def rl(self):
        c=""
        a=""
        while((c)!= "\n"):
            c= self.sock.recv(1)
            print c
            if c=="":
                break
            if c!="\n":
                a=a+c
        return a
    def sendlist(self,data,count):
        print "count " + count
        self.wl(count)
        print "send " + count
        for row in data:
            self.wl(str(row[0]))
            print row[0]

    def revlist(self):
        count=int(self.rl())
        for i in  range(1,count):
            print self.rl()
    def close(self):
        self.sock.close()
    def sendKG(self,kg):
        self.wl("KG")
        self.wl(kg)
    def sendRF(self,rf):
        self.wl("RF")
        self.wl(rf)

class Database:
    def __init__(self,data):
        self.conn = sqlite3.connect(data)
        self.db = self.conn.cursor()
        try:
            global DeviceID,FarmID
            self.createTB()
            self.AddFarm("F1","local")
            FarmID=self.selectFarmIDformFarmname("F1")
            self.AddDeviceToFarm(DeviceID,FarmID)
            print 'Tabal have never Create'
        except sqlite3.DatabaseError,e:
            print  e

    def insertFA(self,data):
        self.db.execute("insert into fname(name) values (?)", (data,))
        self.conn.commit()
    def insertFarm(self,name,address):
        self.db.execute("insert into farm(name,address) values (?,?)", (name,address))
        self.conn.commit()
    def insertFamily(self,name,species,typecode, farmID):
        self.db.execute("insert into family(Name,Species,TypeCode,FarmID) values (?,?,?,?)", (name,species,typecode,farmID))
        self.conn.commit()
    def insertFish(self,FamilyID,RFID,Sex):
        self.db.execute("insert into fish(FamilyID,RFID,Sex) values (?,?,?)", (FamilyID,RFID,Sex))
        self.conn.commit()
    def insertBreader(self,FamilyID,FishID):
        self.db.execute("insert into breader(FamilyID,FishID) values (?,?)", (FamilyID,FishID))
        self.conn.commit()
    def insertMeasurementFish(self,DeviceID,FishID,ImageID,Weight,StandardLength,TotalLength,HeadLength,BodyWidth,BodyDepth):
        self.db.execute("insert into measurementFish(DeviceID,FishID,ImageID,Weight,StandardLength,TotalLength,HeadLength,BodyWidth,BodyDepth) values (?,?,?,?,?,?,?,?,?)", (DeviceID,FishID,ImageID,Weight,StandardLength,TotalLength,HeadLength,BodyWidth,BodyDepth))
        self.conn.commit()
    def insertImage(self,ImagePath):
        self.db.execute("insert into image(ImagePath) values (?)", (ImagePath,))
        self.conn.commit()
    def insertdevice(self,DeviceID,FarmID):
        self.db.execute("insert into device(DeviceID,FarmID) values (?,?)", (DeviceID,FarmID))
        self.conn.commit()

    def pritt(self,data):
        for row in data:
            print row
    def insertFA(self,data):
        self.db.execute("insert into fname(name) values (?)", (data,))
        self.conn.commit()
    def createTB(self):
        self.db.execute('''CREATE TABLE  farm ( FarmID INTEGER  PRIMARY KEY , name TEXT NOT NULL , address TEXT NULL )''')
        self.db.execute('''CREATE TABLE  image ( ImageID INTEGER PRIMARY KEY , ImagePath TEXT NOT NULL) ''')
        self.db.execute('''CREATE TABLE  device ( DeviceID INTEGER   PRIMARY KEY , FarmID INT NOT NULL ,FOREIGN KEY (FarmID) REFERENCES Farm(FarmID) ON DELETE CASCADE  ON UPDATE CASCADE) ''')
        self.db.execute('''CREATE TABLE  family ( FamilyID INTEGER   PRIMARY KEY, Name TEXT  NOT NULL , Species TEXT NULL , TypeCode INTEGER NULL , FarmID INTEGER NOT NULL ,  FOREIGN KEY (FarmID) REFERENCES Farm(FarmID) ON DELETE CASCADE)''')
        self.db.execute('''CREATE TABLE  breader ( FishID INT NOT NULL , FamilyID INT NOT NULL ,   FOREIGN KEY (FishID) REFERENCES Fish(FishID) ,	FOREIGN KEY (FamilyID) REFERENCES family(FamilyID),PRIMARY KEY (FamilyID,FishID))''')
        self.db.execute('''CREATE TABLE  fish ( FishID INTEGER  PRIMARY KEY, FamilyID INT NOT NULL , RFID TEXT NOT NULL, Sex	TEXT UNIQUE NULL,   FOREIGN KEY (FamilyID) REFERENCES Family(FamilyID)                      ON DELETE CASCADE  ON UPDATE CASCADE )''')
        self.db.execute('''CREATE TABLE  measurementFish ( MesID INTEGER  PRIMARY KEY, FishID INT NOT NULL , DeviceID INT NOT NULL, ImageID INT NOT NULL, TimeStamp timestamp default (strftime('%s', 'now')), Weight FLOAT   NULL, StandardLength	FLOAT  NULL, TotalLength FLOAT   NULL, HeadLength FLOAT   NULL, BodyWidth	FLOAT  NULL, BodyDepth	FLOAT  NULL, FOREIGN KEY (DeviceID) REFERENCES Device(DeviceID)                      ON DELETE CASCADE  ON UPDATE CASCADE, FOREIGN KEY (FishID) REFERENCES Fish(FishID)                      ON DELETE CASCADE  ON UPDATE CASCADE,FOREIGN KEY (ImageID) REFERENCES Image(ImageID)                      ON DELETE CASCADE  ON UPDATE CASCADE ) ''')
        self.db.execute('''create table fname (ID INTEGER PRIMARY KEY,name TEXT UNIQUE NOT NULL)''')
        self.conn.commit()
    def selectImageIDFormImagePath(self,ImagePath):
        row= self.db.execute("select ImageID from Image where ImagePath = ?",(ImagePath,))
        for row1 in row:
            return row1[0]
    def selectMas(self):
        row= self.db.execute("select * from measurementFish")
        return row
    def selectNamefamily(self):
        row= self.db.execute("select Name from family")
        return row
    def selectFishIDFormRFID(self,RFID):
        row= self.db.execute("select FishID from fish where RFID = ?",(RFID,))
        for row1 in row:
            return row1[0]

    def selectFamilyIDFormFamilyname(self,Name):
        row= self.db.execute("select FamilyID from family where Name = ?",(Name,))
        for row1 in row:
            return row1[0]

    def selectFarmIDformDeviceID(self,DeviceID):
        row= self.db.execute("select FarmID from device where DeviceID = ?",(DeviceID,))
        for row1 in row:
            return row1[0]
    def selectFarmIDformFarmname(self,Farmname):
        row= self.db.execute("select FarmID from farm where name = ?",(Farmname,))
        for row1 in row:
            return row1[0]


    def selectFamily(self):
        row= self.db.execute("select Name from family")
        return row

    def selectcountFamily(self):
        row= self.db.execute("select count(*) from family")
        data=row.fetchone()[0]
        return str(data)
    def close(self):
        self.db.close()

    def AddFamily(self,name,Deviceid):
        #ADDFamily
        farmid=self.selectFarmIDformDeviceID(Deviceid)
        self.insertFamily(name,"fish","123455",farmid)
    def AddBreader(self,Familyname,RFID):
        #addBreader
        familyid=self.selectFamilyIDFormFamilyname(Familyname)
        fishID=self.selectFishIDFormRFID(RFID)
        self.insertBreader(familyid,fishID)
    def AddBreading(self,Familyname,RFID,sex):
        #addBreading
        familyid=self.selectFamilyIDFormFamilyname(Familyname)
        self.insertFish(familyid,RFID,sex)
    def AddFarm(self,Farmname,FarmAdd):
        #AddFarm
        self.insertFarm(Farmname,FarmAdd)
    def AddDeviceToFarm(self,DeviceID,FarmID):
        self.insertdevice(DeviceID,FarmID)
    def AddMs(self,DeviceID,RFID,ImagePath,Weight,StandardLength,TotalLength,HeadLength,BodyWidth,BodyDepth):
        #MS
        fishID=self.selectFishIDFormRFID(RFID)
        self.insertImage(ImagePath)
        imageID=self.selectImageIDFormImagePath(ImagePath)
        self.insertMeasurementFish(DeviceID,fishID,imageID,Weight,StandardLength,TotalLength,HeadLength,BodyWidth,BodyDepth)
        data=self.selectMas()
        self.pritt(data)

class RFID(threading.Thread):
    def __init__(self,COM,Rate):
        self.COM=COM
        self.Rate=Rate
        print "Start Rfid "
        self.serial = serial.Serial(self.COM,self.Rate) # open first serial port
        print self.serial.portstr + "RFID"
        self.serial.flushInput()
        threading.Thread.__init__(self)

    def ReadID(self):
        Text = self.serial.readline()
        return Text
    def clear(self):
        self.serial.flushInput()
        self.serial.flushOutput()
    def run(self):
        print "Starting RFID "

        global ex_threadflag
        while(not ex_threadflag):
            txtID = self.ReadID()
            Nw.sendRF(txtID)
            queueLock.acquire()
            RfQueue.put(txtID)
            queueLock.release()
        self.serial.close()
        print "RfiD close"

class KG(threading.Thread):
    def __init__(self,COM,Rate):
        self.COM=COM
        self.Rate=Rate
        self.serial1 = serial.Serial( self.COM,self.Rate) # open first serial port
        self.serial1.flushInput()
        print self.serial1.portstr + "KG"
        threading.Thread.__init__(self)

    def ReadKG(self):
        Text = self.serial1.readline()
        return Text
    def clear(self):
        self.serial1.flushInput()
        self.serial1.flushOutput()
    def run(self):
        print "Starting kg "
        global ex_threadflag
        while(not ex_threadflag):
            txtKG = self.ReadKG()
            print txtKG
            Nw.sendKG(txtKG)
            queueLock.acquire()
            KgQueue.put(txtKG)
            queueLock.release()
        self.serial1.close()
        print "Serial Kg close"

class Camera(threading.Thread):
    def __init__(self,callback,family):
        self.Cam =cv2.VideoCapture(-1)
        self.Cam.set(3,800)
        self.Cam.set(4,600)
        self.callback=callback
        self.family=family
        for i in range(1,16):
            print '%s %s' %(i,self.Cam.get(i))

        threading.Thread.__init__(self)
    def ReadCam(self):
        _,self.f=self.Cam.read()
    def SaveCam(self,imagepath):
        cv2.imwrite(imagepath,self.f)

    def run(self):
        print  "Camera start"
        global ex_threadflag
        i=0
        while(not ex_threadflag):
            if (not KgQueue.empty()) :#and (not RfQueue.empty()):
                global gKG ,gRF ,gImagePath
                i=i+1
                queueLock.acquire()
                gKG=KgQueue.get()
                gRF=str(1)#RfQueue.get()
                self.ReadCam()
                Db = Database('example5.db')
                fishid=Db.selectFishIDFormRFID(gRF)
                mid=time.time()
                gImagePath=str(fishid)+"_"+str(mid)+".jpg"
                self.SaveCam(gImagePath)
                self.callback(self.family,gKG,gRF,gImagePath)
                queueLock.release()
                print "Save Image"
        self.Cam.release()
        print "Camera release"

def MS(callback):
    family= Nw.rl()
    global datams,cam,rf,kg,ex_threadflag
    ex_threadflag=0
    cam=Camera(callback,family)
    rf=RFID('/dev/ttyACM0',19200)
    kg=KG('/dev/ttyUSB0',9600)
    rf.start()
    kg.start()
    cam.start()
    threadBack = BackMS()
    threadBack.start()
    datams=""
    threadBack.join()
    ex_threadflag=1
    rf.serial.close()
    kg.serial1.close()
    cam.Cam.release()
    print "out while ms"

def AddBreder(family,Kg,rfids,imagep):
    print "svae Add Breadder"
    Db = Database('example5.db')
    try:
        Db.AddBreader(family,rfids)
        Nw.wl("ok")
    except sqlite3.DatabaseError,e:
        print  e
        Nw.wl("no")
def AddBreading(family,Kg,rfids,imagep):
    print "svae Add Breading"
    Db = Database('example5.db')
    sex="-"
    try:
        Db.AddBreading(family,rfids,sex)
        Nw.wl("ok")
    except sqlite3.DatabaseError,e:
        print  e
        Nw.wl("no")
def AddMeusu(family,Kg,rfids,imagep):
    print "svae Add Mesu"
    Db = Database('example5.db')
    sex="-"
    try:
        Db.AddMs(DeviceID,rfids,imagep,"1","1","1","1","1","1")
        Nw.wl("ok")
    except sqlite3.DatabaseError,e:
        print  e
        Nw.wl("no")
#Insert a row of data
queueLock = threading.Lock()
KgQueue = Queue.Queue(10)
RfQueue = Queue.Queue(10)
Db = Database('example5.db')
Nw = Network('192.168.42.129',6000)

exitFlag=Nw.coned()

while  exitFlag:
    input=Nw.rl()
    print input
    if input!= "":
        if(input=="FA"):
            data=Nw.rl()
            print "insert " +data
            try:
                Db.AddFamily(data,DeviceID)
                Nw.wl("ok")
            except sqlite3.DatabaseError,e:
                print  e
                Nw.wl("no")

        if(input=="LF"):

            print "selectFA "
            count=Db.selectcountFamily()
            data=Db.selectFamily()
            Nw.sendlist(data,count)
            print "e"
        if (input == "ADB"):
            MS(AddBreder)


        if (input == "ADBS"):
            MS(AddBreading)


        if(input=="Bind"):
            Nw.wl("ok")

        if(input=="MS"):
            MS(AddMeusu)


    else:

        Db.close()
        Nw.close()
        print "exit"
        exit()

        time.sleep(0.1)
Db.close()
Nw.close()
print "exit"



