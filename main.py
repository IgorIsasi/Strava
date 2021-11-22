from controllers.StravaAPI import stravaApiKud
import datetime


def getAthlete():
    print("---------------------------------------------")
    atleta=stravaApiKud.getAthlete()
    print("Izena: ",atleta['firstname'])
    print("Abizena: ",atleta['lastname'])
    print("Sexua: ",atleta['sex'])
    print("Oinetakoak: ",atleta['shoes'][0]['name'])
    print("Jarraitzaileak: ",atleta['follower_count'])
    print("---------------------------------------------")


def getActivities():
        egunak=int(input("Duela zenbat eguneko entrenamenduak ikusi nahi dituzu? "))
        today = datetime.datetime.today() #Momentuko data eta ordua
        yesterday=today-datetime.timedelta(days=egunak) #Atzoko data eta ordua
        yesterday=yesterday.timestamp() #Atzoko timestamp
        parametroak={'after':yesterday}# 'before':50, 'page':1, 'per_page':5}
        jarduerak=stravaApiKud.getActivities(parametroak)
        for jarduera in jarduerak:
            getActivitiesId(jarduera["id"])


def div():
    print("")
    print("-------------------------------------------------------")
    print("")
            

def getActivitiesId(id):
    jardueraXehetasunekin=stravaApiKud.getActivityId(id)

    kudos=stravaApiKud.getCommentsByActivityId(jardueraXehetasunekin["id"])
    bidaltzekoDatuak={}

    #ENTRENAMENDURAKO
    bidaltzekoDatuak["id"]=jardueraXehetasunekin['id']
    bidaltzekoDatuak['izena']=jardueraXehetasunekin['name']
    bidaltzekoDatuak['mota']=jardueraXehetasunekin['type']
    bidaltzekoDatuak['hasieraData']=jardueraXehetasunekin['start_date']
    bidaltzekoDatuak['denbora']=jardueraXehetasunekin['elapsed_time']
    #TODO bidaltzekoDatuak['bukaeraData']=dateToSecs(bidaltzekoDatuak['hasieraData'])
    bidaltzekoDatuak['distantzia']=jardueraXehetasunekin['distance']
    bidaltzekoDatuak['ikusgarritasuna']=jardueraXehetasunekin['visibility']
    bidaltzekoDatuak['bzbAbiadura']=jardueraXehetasunekin['average_speed']
    bidaltzekoDatuak['maxAbiadura']=jardueraXehetasunekin['max_speed']
    bidaltzekoDatuak['komentarioak']=[]
    bidaltzekoDatuak['bueltak']=[]
    bidaltzekoDatuak['ekipamendua']={}
    unekoKomentarioa={}
    

    #KUDOS-ERAKO
    for komentario in kudos:
        unekoKomentarioa['komentarioIgorleId']=komentario['id']
        unekoKomentarioa['komentarioIgorleIzena']=komentario["athlete"]["firstname"]
        unekoKomentarioa['komentarioIgorleAbizena']=komentario["athlete"]["lastname"]
        unekoKomentarioa['komentarioTestua']=komentario["text"]
        unekoKomentarioa['komentarioData']=komentario["created_at"]
        bidaltzekoDatuak["komentarioak"].append(unekoKomentarioa)

    
    #EKIPAMENDURAKO
    if jardueraXehetasunekin['gear_id']!=None:
        ekipamendua=stravaApiKud.getEkipamendua(jardueraXehetasunekin['gear_id'])
        bidaltzekoDatuak['ekipamendua']['id']=ekipamendua['id']
        bidaltzekoDatuak['ekipamendua']['marka']=ekipamendua['brand_name']
        bidaltzekoDatuak['ekipamendua']['modeloa']=ekipamendua['model_name']
        bidaltzekoDatuak['ekipamendua']['izena']=ekipamendua['nickname']
        bidaltzekoDatuak['ekipamendua']['distantzia']=ekipamendua['converted_distance']

    #BUELTETARAKO
    bueltak=stravaApiKud.getActivityLaps(id)
    for buelta in bueltak:
        print(buelta)
        unekoBuelta={}
        unekoBuelta['medizioak']={}
        unekoBuelta['id']=buelta['id']
        unekoBuelta['izena']=buelta['name']
        unekoBuelta['distantzia']=buelta['distance']
        unekoBuelta['denbora']=buelta['elapsed_time']
        unekoBuelta['medizioak']['hasieraData']=buelta['start_date_local']
        unekoBuelta['medizioak']['abiaduraBzb']=buelta['average_speed']
        unekoBuelta['medizioak']['abiaduraMax']=buelta['max_speed']
        unekoBuelta['medizioak']['pultsazioBzb']=buelta['average_heartrate']
        unekoBuelta['medizioak']['pultsazioMax']=buelta['max_heartrate']
        bidaltzekoDatuak['bueltak'].append(unekoBuelta)
    




        
    






    


    div()

    




def main():
    if __name__ == '__main__':
        stravaApiKud.getAccessToTheAPI()
        #print(stravaApiKud.getAthlete())
        #em = stravaApiKud.getActivities({})
        #ac = stravaApiKud.getActivityId(em[0]["id"])
        #print(ac["name"], ac["type"], ac["distance"])
        #astr = stravaApiKud.getActivityStreams(em[0]["id"])
        #print(astr)
        #getAthlete()
        getActivities()
        #print(stravaApiKud.getActivityLaps(em[0]['id']))
        
        #getActivitiesID(6202857865)
        #getActivitiesIDStreams()
main()

    
