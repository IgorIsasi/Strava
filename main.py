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
        bidaltzekoDatuak={}
        for jarduera in jarduerak:
            print(jarduera)
            jardueraXehetasunekin=getActivitiesId(jarduera['id'])
            
            bidaltzekoDatuak['mota']=jardueraXehetasunekin['type']
            bidaltzekoDatuak['hasieraData']=jardueraXehetasunekin['start_date']
            bidaltzekoDatuak['denbora']=jardueraXehetasunekin['elapsed_time']
            #TODO bidaltzekoDatuak['bukaeraData']=dateToSecs(bidaltzekoDatuak['hasieraData'])
            bidaltzekoDatuak['ikusgarritasuna']=jardueraXehetasunekin['visibility']
            bidaltzekoDatuak['bzbAbiadura']=jardueraXehetasunekin['average_speed']
            bidaltzekoDatuak['maxAbiadura']=jardueraXehetasunekin['max_speed']
            bidaltzekoDatuak['ekipamenduaID']=jardueraXehetasunekin['gear_id']
        bidaltzekoDatuak={}

        #ENTRENAMENDURAKO
        for i in range(0,len(datuak)):
            
            print(bidaltzekoDatuak)
            if(datuak[i]['gear_id'] is not None):
                emaitza=stravaApiKud.getEkipamendua(datuak[i]['gear_id'])
                

            div()

            
            
            
            #TODO datuak bidali INSERT INTO entrenamenduak VALUES ...

        #JARRAITZAILERAKO


def div():
    print("-------------------------------------------------------")

            

def getActivitiesId(id):
    entrenamendua = stravaApiKud.getActivityId(id)
    print("Id: ", entrenamendua['id'])
    print("Izena: ",entrenamendua['name'])
    print("Data: ",entrenamendua['start_date_local'])
    print("Mota: ",entrenamendua['type'])
    print("Denbora: "),entrenamendua['elapsed_time']
    print("Ikusgarritasuna: ",entrenamendua['visibility'])
    print("Distantzia: ", entrenamendua['distance'])
    print("Batazbesteko abiadura: ", entrenamendua['average_speed'])
    print("Abiadura maximoa: ",entrenamendua['max_speed'])
    print("Pultsometroa: ",entrenamendua['has_heartrate'])
    print("-------------------------------------------------")







if __name__ == '__main__':
    stravaApiKud.getAccessToTheAPI()
    #print(stravaApiKud.getAthlete())
    em = stravaApiKud.getActivities({})
    #ac = stravaApiKud.getActivityId(em[0]["id"])
    #print(ac["name"], ac["type"], ac["distance"])
    #astr = stravaApiKud.getActivityStreams(em[0]["id"])
    #print(astr)
    #getAthlete()
    getActivities()
    #print(stravaApiKud.getActivityLaps(em[0]['id']))

    for i in range(0,len(em)):
        com = stravaApiKud.getCommentsByActivityId(em[i]["id"])
        print(com)
    
    #getActivitiesID(6202857865)
    #getActivitiesIDStreams()

    
