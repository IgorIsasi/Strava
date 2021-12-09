import sqlite3
from controllers.StravaAPI import stravaApiKud
from model import Ekipamendua,Buelta,Entrenamendua

class DBKudeatzailea:
    def konektatu(self):
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
        DatuakGorde.getActivities()
        self.deskonektatu

    def datuakIkusi(self, taula): #SELECT egitean objetua sortu eta ondoren bistaratu objetutik
        self.kur.execute(f"SELECT * FROM {taula}")
        for x in self.kur:
            print(x)

    ####DATUAK DATU BASERA BIDALI   

    #EKIPAMENDUA#
    def ekipamenduaKonprobatu(self,ID,marka,modelo,izena,distantzia):
        self.kur.execute(f"SELECT ID,marka,modelo,izena,distantzia FROM Ekipamendua WHERE ID='{ID}' AND marka='{marka}' AND modelo='{modelo}' AND izena='{izena}' AND distantzia='{distantzia}'")
        emaitza=self.kur.fetchall()
        if len(emaitza)==0:
            self.ekipamenduaBidali(ID,marka,modelo,izena,distantzia)
                 
    def ekipamenduaBidali(self,ID,marka,modelo,izena,distantzia):
        self.kur.execute(f"INSERT OR REPLACE INTO Ekipamendua(ID, marka, modelo, izena, distantzia) VALUES('{ID}', '{marka}', '{modelo}', '{izena}', {distantzia})")

    #ENTRENAMENDUA#
    def entrenamenduaKonprobatu(self,ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax,streamDenborak,streamDistantziak,streamAbiadurak,streamPultsazioak,streamAltitudeak,mapa,streamLatLng):
        self.kur.execute(f"SELECT ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax,streamDenborak,streamDistantziak,streamAbiadurak,streamPultsazioak,streamAltitudeak,mapa,streamLatLng FROM Entrenamendua WHERE ID='{ID}' AND mota='{mota}' AND denbora={denbora} AND izena='{izena}' AND hasieraData='{hasieraData}' AND distantzia={distantzia} AND ikusgarritasuna='{ikusgarritasuna}' AND abiaduraBzb={abiaduraBzb} AND abiaduraMax={abiaduraMax} AND streamDenborak='{streamDenborak}' AND streamDistantziak='{streamDistantziak}' AND streamAbiadurak='{streamAbiadurak}' AND streamPultsazioak='{streamPultsazioak}' AND streamAltitudeak='{streamAltitudeak}' AND mapa='{mapa}' AND streamLatLng='{streamLatLng}'")
        emaitza=self.kur.fetchall()
        if len(emaitza)==0:
            self.entrenamenduaBidali(ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax,streamDenborak,streamDistantziak,streamAbiadurak,streamPultsazioak,streamAltitudeak,mapa,streamLatLng)

    def entrenamenduaBidali(self,ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax,streamDenborak,streamDistantziak,streamAbiadurak,streamPultsazioak,streamAltitudeak,mapa,streamLatLng):
        self.kur.execute(f"INSERT OR REPLACE INTO Entrenamendua(ID, mota, denbora, izena, hasieraData, distantzia, ikusgarritasuna, abiaduraBzb, abiaduraMax, streamDenborak, streamDistantziak, streamAbiadurak, streamPultsazioak, streamAltitudeak, mapa, streamLatLng) VALUES('{ID}', '{mota}', {denbora}, '{izena}', '{hasieraData}', {distantzia}, '{ikusgarritasuna}', {abiaduraBzb}, {abiaduraMax}, '{streamDenborak}', '{streamDistantziak}', '{streamAbiadurak}', '{streamPultsazioak}', '{streamAltitudeak}', '{mapa}', '{streamLatLng}')")

    #JARRAITZAILEA#
    def jarraitzaileaKonprobatu(self,izena,abizena):
        self.kur.execute(f"SELECT izena,abizena FROM Jarraitzaile WHERE izena='{izena}' AND abizena='{abizena}'")       
        emaitza=self.kur.fetchall()
        if len(emaitza)==0:
            self.jarraitzaileaBidali(izena,abizena)

    def jarraitzaileaBidali(self,izena,abizena):
        self.kur.execute(f"INSERT OR REPLACE INTO Jarraitzaile(izena, abizena) VALUES('{izena}', '{abizena}')")

    #KOMENTARIOA#
    def komentarioaKonprobatu(self,izena,abizena,testua,ID,data):
        self.kur.execute(f"self,izena,abizena,testua,ID,data FROM Komentario WHERE izena='{izena}' AND abizena='{abizena}' AND testua='{testua}' AND ID='{ID}' AND data='{data}'")
        emaitza=self.kur.fetchall()
        if len(emaitza)==0:
            self.entrenamenduaBidali(izena,abizena,testua,ID,data)

    def komentarioaBidali(self,izena,abizena,testua,ID,data):
        self.kur.execute(f"INSERT OR REPLACE INTO Komentario(komentarioIgorleIzena, komentarioIgorleAbizena, komentarioTestua, komentarioId, komentarioData) VALUES('{izena}', '{abizena}', '{testua}', '{ID}', '{data}')")

    #BUELTA#
    def bueltaKonprobatu(self,ID,denbora,IDEntrena,izena,distantzia,dataOrdua,abiaduraBzb,abiaduraMax,pultsazioBzb,pultsazioMax,streamStartIndex,streamEndIndex):
        self.kur.execute(f"SELECT ID,denbora,IDEntrena,izena,distantzia,dataOrdua,abiaduraBzb,abiaduraMax,pultsazioBzb,pultsazioMax,streamStartIndex,streamEndIndex FROM Buelta WHERE ID='{ID}' AND denbora='{denbora}' AND IDEntrena='{IDEntrena}' AND izena='{izena}' AND distantzia={distantzia} AND dataOrdua='{dataOrdua}' AND abiaduraBzb={abiaduraBzb} AND abiaduraMax={abiaduraMax} AND pultsazioBzb={pultsazioBzb} AND pultsazioMax={pultsazioMax} AND streamStartIndex='{streamStartIndex}' AND streamEndIndex='{stravaApiKud}'")
        emaitza=self.kur.fetchall()
        if len(emaitza)==0:
            self.bueltaBidali(ID,denbora,IDEntrena,izena,distantzia,dataOrdua,abiaduraBzb,abiaduraMax,pultsazioBzb,pultsazioMax,streamStartIndex,streamEndIndex)

    def bueltaBidali(self,ID,denbora,IDEntrena,izena,distantzia,dataOrdua,abiaduraBzb,abiaduraMax,pultsazioBzb,pultsazioMax,streamStartIndex,streamEndIndex):
        self.kur.execute(f"INSERT OR REPLACE INTO Buelta(ID, denbora, IDEntrena, izena, distantzia, dataOrdua, abiaduraBzb, abiaduraMax, pultsazioBzb, pultsazioMax, streamStartIndex, streamEndIndex) VALUES('{ID}', {denbora}, '{IDEntrena}', '{izena}', {distantzia}, '{dataOrdua}', {abiaduraBzb}, {abiaduraMax}, {pultsazioBzb}, {pultsazioMax}, {streamStartIndex}, {streamEndIndex})")
    
    #SEGMENTUA#
    def segmentuaKonprobatu(self,ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua):
        self.kur.execute(f"SELECT ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua FROM Segmentua WHERE ID='{ID}' AND denbora={denbora} AND izena='{izena}' AND distantzia={distantzia} AND hasieraData='{hasieraData}' AND IDEntrenamendua='{IDEntrenamendua}'")
        emaitza=self.kur.fetchall()
        if len(emaitza)==0:
            self.segmentuaBidali(ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua)

    def segmentuaBidali(self,ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua):
        self.kur.execute(f"INSERT OR REPLACE INTO Segmentua(ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua) VALUES('{ID}', {denbora}, '{izena}', {distantzia}, '{hasieraData}', '{IDEntrenamendua}')")



    #DATUAK IKUSI (KLASEAK SORTUZ)
    def entrenamenduakIkusi(self):
        self.kur.execute("SELECT * FROM Entrenamendua")
        entrenamenduak = []
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
            streamDenborak = atributuak[9]
            streamDistantziak = atributuak[10]
            streamAbiadurak = atributuak[11]
            streamPultsazioak = atributuak[12]
            streamAltitudeak = atributuak[13]
            mapa = atributuak[14]
            streamLatLng = atributuak[15]
            entr = Entrenamendua.Entrenamendua(ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax,streamDenborak,streamDistantziak,streamAbiadurak,streamPultsazioak,streamAltitudeak,mapa,streamLatLng)
            entrenamenduak.append(entr)
        return entrenamenduak

    def entrenamenduakBilatu(self, noiztik, nora, mota):
        entrenamenduak=[]
        if mota == "Guztiak":
            self.kur.execute(f"SELECT * FROM Entrenamendua WHERE hasieraData>='{noiztik}' AND hasieraData<='{nora}'")
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
                streamDenborak = atributuak[9]
                streamDistantziak = atributuak[10]
                streamAbiadurak = atributuak[11]
                streamPultsazioak = atributuak[12]
                streamAltitudeak = atributuak[13]
                mapa = atributuak[14]
                streamLatLng = atributuak[15]
                entr = Entrenamendua.Entrenamendua(ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax,streamDenborak,streamDistantziak,streamAbiadurak,streamPultsazioak,streamAltitudeak,mapa,streamLatLng)
                entrenamenduak.append(entr)
        else:
            self.kur.execute(f"SELECT * FROM Entrenamendua WHERE mota='{mota}' AND hasieraData>='{noiztik}' AND hasieraData<='{nora}'")
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
                streamDenborak = atributuak[9]
                streamDistantziak = atributuak[10]
                streamAbiadurak = atributuak[11]
                streamPultsazioak = atributuak[12]
                streamAltitudeak = atributuak[13]
                mapa = atributuak[14]
                streamLatLng = atributuak[15]
                entr = Entrenamendua.Entrenamendua(ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax,streamDenborak,streamDistantziak,streamAbiadurak,streamPultsazioak,streamAltitudeak,mapa,streamLatLng)
                entrenamenduak.append(entr)
        return entrenamenduak

    def entrenamenduarenBueltakIkusi(self,entrenamendua):
        IDEntrena = entrenamendua.ID
        self.kur.execute(f"SELECT * FROM Buelta WHERE IDEntrena='{IDEntrena}'")
        bueltak = []
        for atributuak in self.kur:
            ID = atributuak[0]
            denbora = atributuak[1]
            IDEntrena = atributuak[2]
            izena = atributuak[3]
            distantzia = atributuak[4]
            dataOrdua = atributuak[5]
            abiaduraBzb = atributuak[6]
            abiaduraMax = atributuak[7]
            pultsazioBzb= atributuak[8]
            pultsazioMax = atributuak[9]
            streamStartIndex = atributuak[10]
            streamEndIndex = atributuak[11]
            buel = Buelta.Buelta(ID,denbora,IDEntrena,izena,distantzia,dataOrdua,abiaduraBzb,abiaduraMax,pultsazioBzb,pultsazioMax,streamStartIndex,streamEndIndex)
            bueltak.append(buel)
        return bueltak

    def ekipamenduenDistantziaIkusi(self):
        ekipamenduak = []
        self.kur.execute("SELECT * FROM Ekipamendua")
        for atributuak in self.kur:
            ID = atributuak[0]
            marka = atributuak[1]
            modelo = atributuak[2]
            izena = atributuak[3]
            distantzia = atributuak[4]
            ek = Ekipamendua.Ekipamendua(ID,marka,modelo,izena,distantzia)
            ekipamenduak.append(ek)
        return ekipamenduak


kudeatzaile=DBKudeatzailea()
import DatuakGorde #behean circular import errorea ez agertzeko