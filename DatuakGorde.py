from controllers.StravaAPI import stravaApiKud
from controllers.DBKudeatzailea.DBKud import kudeatzaile

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
    stream=stravaApiKud.getActivityStreams(id)
    
    #EKIPAMENDURAKO
    try: #konprobatu ekipamendua badagoela
        ekipamendua=stravaApiKud.getEkipamendua(jardueraXehetasunekin['gear_id'])
        idEk=ekipamendua['id']
        try: #konprobatu ekipamenduaren atributuak badaudela
            markaEk=ekipamendua['brand_name']
            modeloEk=ekipamendua['model_name']
            izenaEk=ekipamendua['nickname']
            distantziaEk=ekipamendua['converted_distance']
        except:
            markaEk=None
            modeloEk=None
            izenaEk=None
            distantziaEk=None
        kudeatzaile.ekipamenduaKonprobatu(idEk,markaEk,modeloEk,izenaEk,distantziaEk)
    except:
        print("Ez dago ekipamendurik")


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
    try:
        streamDenborakEn=stream["time"]["data"]
        streamDistantziakEn=stream['distance']['data']
        streamAbiadurakEn=stream["velocity_smooth"]["data"]
        streamPultsazioakEn=stream["heartrate"]["data"]
        streamAltitudeakEn=stream["altitude"]["data"]
        streamLatLngEn=stream['latlng']['data']
        mapaEn=jardueraXehetasunekin['map']['polyline']
    except:
        streamDenborakEn=None
        streamDistantziakEn=None
        streamAbiadurakEn=None
        streamPultsazioakEn=None
        streamAltitudeakEn=None
        streamLatLngEn=None
        mapaEn=None

    kudeatzaile.entrenamenduaKonprobatu(idEn,motaEn,denboraEn,izenaEn,hasieraDataEn,distantziaEn,ikusgarritasunaEn,abiaduraBzbEn,abiaduraMaxEn,streamDenborakEn,streamDistantziakEn,streamAbiadurakEn,streamPultsazioakEn,streamAltitudeakEn,mapaEn,streamLatLngEn)
    

    #KUDOS-ERAKO
    try:
        kudos=stravaApiKud.getCommentsByActivityId(jardueraXehetasunekin["id"])
        for komentario in kudos:
            #JARRAITZAILERAKO
            izenaJarr=komentario["athlete"]["firstname"]
            abizenaJarr=komentario["athlete"]["lastname"]

            kudeatzaile.jarraitzaileaKonprobatu(izenaJarr,abizenaJarr)

            #KOMENTARIOETARAKO
            idKom=komentario['id']
            testuaKom=komentario["text"]
            dataKom=komentario["created_at"]

            kudeatzaile.komentarioaKonprobatu(izenaJarr,abizenaJarr,testuaKom,idKom,dataKom)
    except:
        print("Ez dago komentariorik:",id)


    #BUELTETARAKO 
    bueltak=jardueraXehetasunekin['laps']
    for buelta in bueltak:
        idBu=buelta['id']
        izenaBu=buelta['name']
        distantziaBu=buelta['distance']
        denboraBu=buelta['elapsed_time']
        dataOrduaBu=buelta['start_date_local']
        dataOrduaBu.replace('T', ' ')
        dataOrduaBu.replace('Z', ' ')
        abiaduraBzbBu=buelta['average_speed']
        abiaduraMaxBu=buelta['max_speed']
        streamStartIndexBu=buelta['start_index']
        streamEndIndexBu=buelta['end_index']
        try:
            pultsazioBzbBu=buelta['average_heartrate']
            pultsazioMaxBu=buelta['max_heartrate']
        except:
            pultsazioBzbBu=None
            pultsazioMaxBu=None

        kudeatzaile.bueltaKonprobatu(idBu,denboraBu,idEn,izenaBu,distantziaBu,dataOrduaBu,abiaduraBzbBu,abiaduraMaxBu,pultsazioBzbBu,pultsazioMaxBu,streamStartIndexBu,streamEndIndexBu)

    #SEGMENTUETARAKO
    try:
        segmentuak=jardueraXehetasunekin['segment_efforts']
        for segmentua in segmentuak:
            idSeg=segmentua['segment']['id']
            izenaSeg=segmentua['segment']['name']
            distantziaSeg=segmentua['segment']['distance']   
            hasieraDataSeg=segmentua['start_date_local']
            denboraSeg=segmentua['elapsed_time']

            kudeatzaile.segmentuaKonprobatu(idSeg,denboraSeg,izenaSeg,distantziaSeg,hasieraDataSeg,idEn)
    except:
        print("Segmentua ezin izan da sartu")