__author__ = 'ober'
import sqlite3
DeviceID="1234"
class Database:
    def __init__(self,data):
        self.conn = sqlite3.connect(data)
        self.db = self.conn.cursor()
        try:
            global DeviceID,FarmID
            self.createTB()
            self.AddFarm("F1","local")
            FarmID=self.selectFamilyIDFormFamilyname("F1")
            self.AddDeviceToFarm(DeviceID,FarmID)
            print 'Tabal have never Create'
        except:
            print 'Tabal have Been Create'

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
        self.db.execute('''CREATE TABLE  family ( FamilyID INTEGER   PRIMARY KEY, Name TEXT NOT NULL , Species TEXT NULL , TypeCode INTEGER NULL , FarmID INTEGER NOT NULL ,  FOREIGN KEY (FarmID) REFERENCES Farm(FarmID) ON DELETE CASCADE)''')
        self.db.execute('''CREATE TABLE  breader ( FishID INT NOT NULL , FarmID INT NOT NULL ,   FOREIGN KEY (FishID) REFERENCES Fish(FishID)                      ON DELETE CASCADE  ON UPDATE CASCADE,	FOREIGN KEY (FishID) REFERENCES Fish(FishID)                     ON DELETE CASCADE  ON UPDATE CASCADE )''')
        self.db.execute('''CREATE TABLE  fish ( FishID INTEGER  PRIMARY KEY, FamilyID INT NOT NULL , RFID TEXT NOT NULL, Sex	TEXT  NULL,   FOREIGN KEY (FamilyID) REFERENCES Family(FamilyID)                      ON DELETE CASCADE  ON UPDATE CASCADE )''')
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
        familyid=DB.selectFamilyIDFormFamilyname(Familyname)
        fishID=self.selectFishIDFormRFID(RFID)
        self.insertBreader(familyid,fishID)
    def AddBreading(self,Familyname,RFID,sex):
        #addBreading
        familyid=DB.selectFamilyIDFormFamilyname(Familyname)
        DB.insertFish(familyid,RFID,sex)
    def AddFarm(self,Farmname,FarmAdd):
        #AddFarm
        DB.insertFarm(Farmname,FarmAdd)
    def AddDeviceToFarm(self,DeviceID,FarmID):
        DB.insertdevice(DeviceID,FarmID)
    def AddMs(self,DeviceID,RFID,ImagePath,Weight,StandardLength,TotalLength,HeadLength,BodyWidth,BodyDepth):
        #MS
        fishID=DB.selectFishIDFormRFID(RFID)
        DB.insertImage(ImagePath)
        imageID=DB.selectImageIDFormImagePath(ImagePath)
        DB.insertMeasurementFish(DeviceID,fishID,imageID,Weight,StandardLength,TotalLength,HeadLength,BodyWidth,BodyDepth)
        data=DB.selectMas()
        DB.pritt(data)


DB=Database('example2')
DB.AddFarm("F1","local")
FarmID=DB.selectFarmIDformFarmname("F1")
print FarmID
DB.AddDeviceToFarm(DeviceID,FarmID)
print FarmID
#data=DB.insertFA('1234')
#DB.db.execute("insert into farm(name,address) values (?,?)", ("f1","22000",))









