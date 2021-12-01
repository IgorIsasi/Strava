import sqlite3
import datuakGorde
from controllers.StravaAPI import stravaApiKud
from model import Ekipamendua,Jarraitzaile,Komentario,Buelta,Entrenamendua,Medizioa,Segmentua

class DBKudeatzailea:
    def konektatu(self):
        print("alo")
        #self.kon = mysql.connector.connect(host="localhost",user="strava",password="patata")
        #self.kur = self.kon.cursor()
        self.kon = sqlite3.connect("strava.db")
        self.kur = self.kon.cursor()
        with open('strava.sql') as db:
            dbString = db.read()
        self.kur.executescript(dbString)
        

    def deskonektatu(self):
        self.kur.close()
        self.kon.close()

    def kargatuDB(self):
        self.konektatu()
        stravaApiKud.getAccessToTheAPI()
        datuakGorde.getActivities(self)
        self.datuakIkusi("Ekipamendua")
        self.ekipamenduaIkusi()
        self.entrenamenduaIkusi()
        self.jarraitzaileaIkusi()
        self.komentarioaIkusi()
        self.bueltaIkusi()
        self.medizioaIkusi()
        self.segmentuaIkusi()
        #self.datuakIkusi("Entrenamendua")
        #self.datuakIkusi("Jarraitzaile")
        #self.datuakIkusi("Komentario")
        #self.datuakIkusi("Buelta")
        #self.datuakIkusi("Medizioak")
        #self.datuakIkusi("Segmentua")
        self.deskonektatu

    def datuakIkusi(self, taula): #SELECT egitean objetua sortu eta ondoren bistaratu objetutik
        self.kur.execute(f"SELECT * FROM {taula}")
        for x in self.kur:
            print(x)

    def ekipamenduaKonprobatu(self,ID,marka,modelo,izena,distantzia):
        self.kur.execute(f"SELECT ID,marka,modelo,izena,distantzia FROM Ekipamendua WHERE ID='{ID}' AND marka='{marka}' AND modelo='{modelo}' AND izena='{izena}' AND distantzia='{distantzia}'")
        print(self.kur.description)
        emaitza=len(self.kur.description)
        if emaitza==0:
            print("Datua ez zegoen beraz bidaliko dut")
            self.ekipamenduaBidali(ID,marka,modelo,izena,distantzia)
        else:
            print("Datua bazegoen beraz ez dut bidaliko")
            

        



    #DATUAK DATU BASERA BIDALI     
    def ekipamenduaBidali(self,ID,marka,modelo,izena,distantzia):
        self.kur.execute(f"INSERT OR REPLACE INTO Ekipamendua(ID, marka, modelo, izena, distantzia) VALUES('{ID}', '{marka}', '{modelo}', '{izena}', {distantzia})")

    def entrenamenduaBidali(self,ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax):
        self.kur.execute(f"INSERT OR REPLACE INTO Entrenamendua(ID, mota, denbora, izena, hasieraData, distantzia, ikusgarritasuna, abiaduraBzb, abiaduraMax) VALUES('{ID}', '{mota}', {denbora}, '{izena}', '{hasieraData}', {distantzia}, '{ikusgarritasuna}', {abiaduraBzb}, {abiaduraMax})")

    def jarraitzaileaBidali(self,izena,abizena):
        self.kur.execute(f"INSERT OR REPLACE INTO Jarraitzaile(izena, abizena) VALUES('{izena}', '{abizena}')")

    def komentarioaBidali(self,izena,abizena,testua,ID,data):
        self.kur.execute(f"INSERT OR REPLACE INTO Komentario(komentarioIgorleIzena, komentarioIgorleAbizena, komentarioTestua, komentarioId, komentarioData) VALUES('{izena}', '{abizena}', '{testua}', '{ID}', '{data}')")

    def bueltaBidali(self,ID,denbora,IDEntrena,izena,distantzia):
        self.kur.execute(f"INSERT OR REPLACE INTO Buelta(ID, denbora, IDEntrena, izena, distantzia) VALUES('{ID}', {denbora}, '{IDEntrena}', '{izena}', {distantzia})")

    def medizioaBidali(self,dataOrdua,IDBuelta,pultsazioBzb,pultsazioMax,abiaduraBzb,abiaduraMax):
        self.kur.execute(f"INSERT OR REPLACE INTO Medizioak(dataOrdua,IDBuelta,pultsazioBzb,pultsazioMax,abiaduraBzb,abiaduraMax) VALUES('{dataOrdua}', '{IDBuelta}', {pultsazioBzb}, {pultsazioMax}, {abiaduraBzb}, {abiaduraMax})")

    def segmentuaBidali(self,ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua):
        self.kur.execute(f"INSERT OR REPLACE INTO Segmentua(ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua) VALUES('{ID}', {denbora}, '{izena}', {distantzia}, '{hasieraData}', '{IDEntrenamendua}')")



    #DATUAK IKUSI (KLASEAK SORTUZ)
    def ekipamenduaIkusi(self):
        self.kur.execute(f"SELECT * FROM Ekipamendua")
        for atributuak in self.kur:
            ID = atributuak[0]
            marka = atributuak[1]
            modelo = atributuak[2]
            izena = atributuak[3]
            distantzia = atributuak[4]
            ek = Ekipamendua.Ekipamendua(ID,marka,modelo,izena,distantzia)
            print(ek.ID,ek.marka,ek.modelo,ek.izena,ek.distantzia)    

    def entrenamenduaIkusi(self):
        self.kur.execute(f"SELECT * FROM Entrenamendua")
        for atributuak in self.kur:
            ID = atributuak[0]
            mota = atributuak[1]
            denbora = atributuak[2]
            izena = atributuak[3]
            hasieraData = atributuak[4]
            distantzia = atributuak[5]
            ikusgarritasuna = atributuak[6]
            abiaduraBzb = atributuak[7]
            abiaduraMax = atributuak[8]
            entr = Entrenamendua.Entrenamendua(ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax)
            print(entr.ID,entr.mota,entr.denbora,entr.izena,entr.hasieraData,entr.distantzia,entr.ikusgarritasuna,entr.abiaduraBzb,entr.abiaduraMax)

    def jarraitzaileaIkusi(self):
        self.kur.execute(f"SELECT * FROM Jarraitzailea")
        for atributuak in self.kur:
            izena = atributuak[0]
            abizena = atributuak[1]
            jarr = Jarraitzaile.Jarraitzaile(izena,abizena)
            print(jarr.izena,jarr.abizena)

    def komentarioaIkusi(self):
        self.kur.execute(f"SELECT * FROM Komentarioa")
        for atributuak in self.kur:
            izena = atributuak[0]
            abizena = atributuak[1]
            testua = atributuak[2]
            ID = atributuak[3]
            data = atributuak[4]
            kom = Komentario.Komentario(izena,abizena,testua,ID,data)
            print(kom.izena,kom.abizena,kom.testua,kom.ID,kom.data)

    def bueltaIkusi(self):
        self.kur.execute(f"SELECT * FROM Buelta")
        for atributuak in self.kur:
            ID = atributuak[0]
            denbora = atributuak[1]
            IDEntrena = atributuak[2]
            izena = atributuak[3]
            distantzia = atributuak[4]
            buel = Buelta.Buelta(ID,denbora,IDEntrena,izena,distantzia)
            print(buel.ID,buel.denbora,buel.IDEntrena,buel.izena,buel.distantzia)

    def medizioaIkusi(self):
        self.kur.execute(f"SELECT * FROM Medizioak")
        for atributuak in self.kur:
            dataOrdua = atributuak[0]
            IDBuelta = atributuak[1]
            pultsazioBzb = atributuak[2]
            pultsazioMax = atributuak[3]
            abiaduraBzb = atributuak[4]
            abiaduraMax = atributuak[5]
            med = Medizioa.Medizioa(dataOrdua,IDBuelta,pultsazioBzb,pultsazioMax,abiaduraBzb,abiaduraMax)
            print(med.dataOrdua,med.IDBuelta,med.pultsazioBzb,med.pultsazioMax,med.abiaduraBzb,med.abiaduraMax)

    def segmentuaIkusi(self):
        self.kur.execute(f"SELECT * FROM Segmentua")
        for atributuak in self.kur:
            ID = atributuak[0]
            denbora = atributuak[1]
            izena = atributuak[2]
            distantzia = atributuak[3]
            hasieraData = atributuak[4]
            IDEntrenamendua = atributuak[5]
            seg = Segmentua.Segmentua(ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua)
            print(seg.ID,seg.denbora,seg.izena,seg.distantzia,seg.hasieraData,seg.IDEntrenamendua)

kudeatzaile=DBKudeatzailea()