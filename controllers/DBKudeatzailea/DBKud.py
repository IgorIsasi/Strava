#import mysql.connector
import sqlite3
import datuakGorde
from controllers.StravaAPI import stravaApiKud

class DBKudeatzailea:
    def konektatu(self):
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
        self.datuakIkusi("Entrenamendua")
        self.datuakIkusi("Jarraitzaile")
        self.datuakIkusi("Komentario")
        self.datuakIkusi("Buelta")
        self.datuakIkusi("Medizioak")
        self.datuakIkusi("Segmentua")
        self.deskonektatu

    def datuakIkusi(self, taula):
        self.kur.execute(f"SELECT * FROM {taula}")
        for x in self.kur:
            print(x)

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