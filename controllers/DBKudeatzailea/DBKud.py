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

    def tablak(self):
        self.kur.execute("SHOW TABLES")
        for x in self.kur:
            print(x)
