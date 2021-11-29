import mysql.connector

class DBKudeatzailea:
    #kon = mysql.connector.connect(host="localhost",user="strava",password="patata",database="strava")
    #kur = kon.cursor()

    def konektatu(self):
        self.kon = mysql.connector.connect(host="localhost",user="strava",password="patata",database="strava")
        self.kur = self.kon.cursor()

    def deskonektatu(self):
        self.kon.close()
        self.kur.close()

    #def datuakBidali(self, datuak):
        #self.kur.execute(f"INSERT INTO Ekipamendua(ID,marka,modelo,izena,distantzia) VALUES({datuak['ekipamendua']['id']},{datuak['ekipamendua']['marka']},{datuak['ekipamendua']['modeloa']},{datuak['ekipamendua']['izena']},{datuak['ekipamendua']['distantzia']})")

    def datuakIkusi(self, taula):
        self.kur.execute(f"SELECT * FROM {taula}")
        for x in self.kur:
            print(x)

    def ekipamenduaBidali(self,ID,marka,modelo,izena,distantzia):
        self.kur.execute(f"INSERT INTO Ekipamendua(ID, marka, modelo, izena, distantzia) VALUES('{ID}', '{marka}', '{modelo}', '{izena}', {distantzia})")

    def entrenamenduaBidali(self,ID,mota,denbora,izena,hasieraData,distantzia,ikusgarritasuna,abiaduraBzb,abiaduraMax):
        self.kur.execute(f"INSERT INTO Entrenamendua(ID, mota, denbora, izena, hasieraData, distantzia, ikusgarritasuna, abiaduraBzb, abiaduraMax) VALUES('{ID}', '{mota}', {denbora}, '{izena}', '{hasieraData}', {distantzia}, '{ikusgarritasuna}', {abiaduraBzb}, {abiaduraMax})")

    def jarraitzaileaBidali(self,izena,abizena):
        self.kur.execute(f"INSERT INTO Jarraitzaile(izena, abizena) VALUES('{izena}', '{abizena}')")

    def komentarioaBidali(self,izena,abizena,testua,ID,data):
        self.kur.execute(f"INSERT INTO Komentario(komentarioIgorleIzena, komentarioIgorleAbizena, komentarioTestua, komentarioId, komentarioData) VALUES('{izena}', '{abizena}', '{testua}', '{ID}', '{data}')")

    def bueltaBidali(self,ID,denbora,IDEntrena,izena,distantzia):
        self.kur.execute(f"INSERT INTO Buelta(ID, denbora, IDEntrena, izena, distantzia) VALUES('{ID}', {denbora}, '{IDEntrena}', '{izena}', {distantzia})")

    def medizioaBidali(self,dataOrdua,IDBuelta,pultsazioBzb,pultsazioMax,abiaduraBzb,abiaduraMax):
        self.kur.execute(f"INSERT INTO Medizioak(dataOrdua,IDBuelta,pultsazioBzb,pultsazioMax,abiaduraBzb,abiaduraMax) VALUES('{dataOrdua}', '{IDBuelta}', {pultsazioBzb}, {pultsazioMax}, {abiaduraBzb}, {abiaduraMax})")

    def segmentuaBidali(self,ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua):
        self.kur.execute(f"INSERT INTO Segmentua(ID,denbora,izena,distantzia,hasieraData,IDEntrenamendua) VALUES('{ID}', {denbora}, '{izena}', {distantzia}, '{hasieraData}', '{IDEntrenamendua}')")