from controllers.StravaAPI import stravaApiKud
from controllers.DBKudeatzailea import DBKud
import datetime
import mysql.connector


#def getAthlete():
    #print("---------------------------------------------")
    #atleta=stravaApiKud.getAthlete()
    #print("Izena: ",atleta['firstname'])
    #print("Abizena: ",atleta['lastname'])
    #print("Sexua: ",atleta['sex'])
    #print("Oinetakoak: ",atleta['shoes'][0]['name'])
    #print("Jarraitzaileak: ",atleta['follower_count'])
    #print("---------------------------------------------")


def getActivities(DBKud):    
        egunak=int(input("Duela zenbat eguneko entrenamenduak ikusi nahi dituzu? "))
        today = datetime.datetime.today() #Momentuko data eta ordua
        yesterday=today-datetime.timedelta(days=egunak) #Atzoko data eta ordua
        yesterday=yesterday.timestamp() #Atzoko timestamp
        parametroak={'after':yesterday}# 'before':50, 'page':1, 'per_page':5}
        jarduerak=stravaApiKud.getActivities(parametroak)
        for jarduera in jarduerak:
            getActivitiesId(DBKud, jarduera["id"])


def div():
    print("")
    print("-------------------------------------------------------")
    print("")
            

def getActivitiesId(DBKud, id):
    jardueraXehetasunekin=stravaApiKud.getActivityId(id)

    kudos=stravaApiKud.getCommentsByActivityId(jardueraXehetasunekin["id"])
    #bidaltzekoDatuak={}
    heartrateDauka=jardueraXehetasunekin['has_heartrate']
    
    #EKIPAMENDURAKO
    if jardueraXehetasunekin['gear_id']!=None:
        ekipamendua=stravaApiKud.getEkipamendua(jardueraXehetasunekin['gear_id'])
        #bidaltzekoDatuak['ekipamendua']['id']=ekipamendua['id']
        #bidaltzekoDatuak['ekipamendua']['marka']=ekipamendua['brand_name']
        #bidaltzekoDatuak['ekipamendua']['modeloa']=ekipamendua['model_name']
        #bidaltzekoDatuak['ekipamendua']['izena']=ekipamendua['nickname']
        #bidaltzekoDatuak['ekipamendua']['distantzia']=ekipamendua['converted_distance']
        
        idEk=ekipamendua['id']
        markaEk=ekipamendua['brand_name']
        modeloEk=ekipamendua['model_name']
        izenaEk=ekipamendua['nickname']
        distantziaEk=ekipamendua['converted_distance']
        #print(id,marka,modelo,izena,distantzia)

        DBKud.ekipamenduaBidali(idEk,markaEk,modeloEk,izenaEk,distantziaEk)



    #ENTRENAMENDURAKO
    #bidaltzekoDatuak["id"]=jardueraXehetasunekin['id']
    #bidaltzekoDatuak['izena']=jardueraXehetasunekin['name']
    #bidaltzekoDatuak['mota']=jardueraXehetasunekin['type']
    #bidaltzekoDatuak['hasieraData']=jardueraXehetasunekin['start_date']
    #bidaltzekoDatuak['denbora']=jardueraXehetasunekin['elapsed_time']
    #TODO bidaltzekoDatuak['bukaeraData']=dateToSecs(bidaltzekoDatuak['hasieraData'])
    #bidaltzekoDatuak['distantzia']=jardueraXehetasunekin['distance']
    #bidaltzekoDatuak['ikusgarritasuna']=jardueraXehetasunekin['visibility']
    #bidaltzekoDatuak['abiaduraBzb']=jardueraXehetasunekin['average_speed']
    #bidaltzekoDatuak['abiaduraMax']=jardueraXehetasunekin['max_speed']
    #bidaltzekoDatuak['komentarioak']=[]
    #bidaltzekoDatuak['bueltak']=[]
    #bidaltzekoDatuak['segmentuak']=[]
    #bidaltzekoDatuak['ekipamendua']={}
    #unekoKomentarioa={}

    idEn=jardueraXehetasunekin['id']
    izenaEn=jardueraXehetasunekin['name']
    motaEn=jardueraXehetasunekin['type']
    hasieraDataEn=jardueraXehetasunekin['start_date']
    denboraEn=jardueraXehetasunekin['elapsed_time']
    #TODO bidaltzekoDatuak['bukaeraData']=dateToSecs(bidaltzekoDatuak['hasieraData'])
    distantziaEn=jardueraXehetasunekin['distance']
    ikusgarritasunaEn=jardueraXehetasunekin['visibility']
    abiaduraBzbEn=jardueraXehetasunekin['average_speed']
    abiaduraMaxEn=jardueraXehetasunekin['max_speed']

    DBKud.entrenamenduaBidali(idEn,motaEn,denboraEn,izenaEn,hasieraDataEn,distantziaEn,ikusgarritasunaEn,abiaduraBzbEn,abiaduraMaxEn)
    

    #KUDOS-ERAKO
    for komentario in kudos:
        #JARRAITZAILERAKO
        izenaJarr=komentario["athlete"]["firstname"]
        abizenaJarr=komentario["athlete"]["lastname"]

        DBKud.jarraitzaileaBidali(izenaJarr,abizenaJarr)

        #KOMENTARIOETARAKO
        idKom=komentario['id']
        testuaKom=komentario["text"]
        dataKom=komentario["created_at"]

        DBKud.komentarioaBidali(izenaJarr,abizenaJarr,testuaKom,idKom,dataKom)

        #bidaltzekoDatuak["komentarioak"].append(unekoKomentarioa)


    #BUELTETARAKO  //TODO BERRIRO PLANTEATU
    bueltak=jardueraXehetasunekin['laps']
    for buelta in bueltak:
        #unekoBuelta={}
        #unekoBuelta['medizioak']={}
        #unekoBuelta['id']=buelta['id']
        #unekoBuelta['izena']=buelta['name']
        #unekoBuelta['distantzia']=buelta['distance']
        #unekoBuelta['denbora']=buelta['elapsed_time']
        #unekoBuelta['medizioak']['dataOrdua']=buelta['start_date_local']
        #unekoBuelta['medizioak']['abiaduraBzb']=buelta['average_speed']
        #unekoBuelta['medizioak']['abiaduraMax']=buelta['max_speed']

        idBu=buelta['id']
        izenaBu=buelta['name']
        distantziaBu=buelta['distance']
        denboraBu=buelta['elapsed_time']

        DBKud.bueltaBidali(idBu,denboraBu,idEn,izenaBu,distantziaBu)

        #MEDIZIOETARAKO
        dataOrduaMe=buelta['start_date_local']
        abiaduraBzbMe=buelta['average_speed']
        abiaduraMaxMe=buelta['max_speed']
        pultsazioBzbMe=None
        pultsazioMaxMe=None

        if(heartrateDauka):
            pultsazioBzbMe=buelta['average_heartrate']
            pultsazioMaxMe=buelta['max_heartrate']
        #bidaltzekoDatuak['bueltak'].append(unekoBuelta)

        DBKud.medizioaBidali(dataOrduaMe,idBu,pultsazioBzbMe,pultsazioMaxMe,abiaduraBzbMe,abiaduraMaxMe)

    #SEGMENTUETARAKO
    segmentuak=jardueraXehetasunekin['segment_efforts']
    for segmentua in segmentuak:
        #unekoSegmentua={}
        #unekoSegmentua['id']=segmentua['segment']['id']
        #unekoSegmentua['izena']=segmentua['segment']['name']
        #unekoSegmentua['distantzia']=segmentua['segment']['distance']   
        #unekoSegmentua['hasieraData']=segmentua['start_date_local']
        #unekoSegmentua['denbora']=segmentua['elapsed_time']
        #bidaltzekoDatuak['segmentuak'].append(unekoSegmentua)

        idSeg=segmentua['segment']['id']
        izenaSeg=segmentua['segment']['name']
        distantziaSeg=segmentua['segment']['distance']   
        hasieraDataSeg=segmentua['start_date_local']
        denboraSeg=segmentua['elapsed_time']

        #DBKud.segmentuaBidali(idSeg,denboraSeg,izenaSeg,distantziaSeg,hasieraDataSeg,idEn)