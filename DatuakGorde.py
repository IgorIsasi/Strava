from controllers.StravaAPI import stravaApiKud
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import datetime

def getActivities():    
        jarduerak=stravaApiKud.getActivities()
        for jarduera in jarduerak:
            getActivitiesId(jarduera["id"])


def div():
    print("")
    print("-------------------------------------------------------")
    print("")
            

def getActivitiesId(id):
    jardueraXehetasunekin=stravaApiKud.getActivityId(id)
    
    kudos=stravaApiKud.getCommentsByActivityId(jardueraXehetasunekin["id"])
    heartrateDauka=jardueraXehetasunekin['has_heartrate']
    
    #EKIPAMENDURAKO
    if jardueraXehetasunekin['gear_id']!=None:
        ekipamendua=stravaApiKud.getEkipamendua(jardueraXehetasunekin['gear_id'])
        
        idEk=ekipamendua['id']
        markaEk=ekipamendua['brand_name']
        modeloEk=ekipamendua['model_name']
        izenaEk=ekipamendua['nickname']
        distantziaEk=ekipamendua['converted_distance']
        kudeatzaile.ekipamenduaBidali(idEk,markaEk,modeloEk,izenaEk,distantziaEk)
        #kudeatzaile.ekipamenduaKonprobatu(idEk,markaEk,modeloEk,izenaEk,distantziaEk)


    #ENTRENAMENDURAKO
    idEn=jardueraXehetasunekin['id']
    izenaEn=jardueraXehetasunekin['name']
    motaEn=jardueraXehetasunekin['type']
    hasieraD=jardueraXehetasunekin['start_date']
    hasieraDataEn=hasieraD.replace('T', ' ')
    hasieraDataEn=hasieraDataEn.replace('Z', ' ')
    denboraEn=jardueraXehetasunekin['elapsed_time']
    distantziaEn=jardueraXehetasunekin['distance']
    ikusgarritasunaEn=jardueraXehetasunekin['visibility']
    abiaduraBzbEn=jardueraXehetasunekin['average_speed']
    abiaduraMaxEn=jardueraXehetasunekin['max_speed']

    kudeatzaile.entrenamenduaBidali(idEn,motaEn,denboraEn,izenaEn,hasieraDataEn,distantziaEn,ikusgarritasunaEn,abiaduraBzbEn,abiaduraMaxEn)
    

    #KUDOS-ERAKO
    for komentario in kudos:
        #JARRAITZAILERAKO
        izenaJarr=komentario["athlete"]["firstname"]
        abizenaJarr=komentario["athlete"]["lastname"]

        kudeatzaile.jarraitzaileaBidali(izenaJarr,abizenaJarr)

        #KOMENTARIOETARAKO
        idKom=komentario['id']
        testuaKom=komentario["text"]
        dataKom=komentario["created_at"]

        kudeatzaile.komentarioaBidali(izenaJarr,abizenaJarr,testuaKom,idKom,dataKom)


    #BUELTETARAKO  //TODO BERRIRO PLANTEATU
    bueltak=jardueraXehetasunekin['laps']
    for buelta in bueltak:
        idBu=buelta['id']
        izenaBu=buelta['name']
        distantziaBu=buelta['distance']
        denboraBu=buelta['elapsed_time']

        kudeatzaile.bueltaBidali(idBu,denboraBu,idEn,izenaBu,distantziaBu)

        #MEDIZIOETARAKO
        dataOrduaMe=buelta['start_date_local']
        abiaduraBzbMe=buelta['average_speed']
        abiaduraMaxMe=buelta['max_speed']
        pultsazioBzbMe='NULL'
        pultsazioMaxMe='NULL'

        if(heartrateDauka):
            pultsazioBzbMe=buelta['average_heartrate']
            pultsazioMaxMe=buelta['max_heartrate']

        kudeatzaile.medizioaBidali(dataOrduaMe,idBu,pultsazioBzbMe,pultsazioMaxMe,abiaduraBzbMe,abiaduraMaxMe)

    #SEGMENTUETARAKO
    segmentuak=jardueraXehetasunekin['segment_efforts']
    for segmentua in segmentuak:
        idSeg=segmentua['segment']['id']
        izenaSeg=segmentua['segment']['name']
        distantziaSeg=segmentua['segment']['distance']   
        hasieraDataSeg=segmentua['start_date_local']
        denboraSeg=segmentua['elapsed_time']

        kudeatzaile.segmentuaBidali(idSeg,denboraSeg,izenaSeg,distantziaSeg,hasieraDataSeg,idEn)