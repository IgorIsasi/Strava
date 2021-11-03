from controllers.StravaAPI import stravaApiKud
import datetime



def getActivities():
        egunak=int(input("Duela zenbat eguneko entrenamenduak ikusi nahi dituzu? "))
        today = datetime.datetime.today() #Momentuko data eta ordua
        yesterday=today-datetime.timedelta(days=egunak) #Atzoko data eta ordua
        yesterday=yesterday.timestamp() #Atzoko timestamp
        parametroak={'after':yesterday}# 'before':50, 'page':1, 'per_page':5}
        r=stravaApiKud.getActivities(parametroak)
        print("-------------------------------------------------")
        for entrenamendua in r:
            print("Izena: ",entrenamendua['name'])
            print("Data: ",entrenamendua['start_date_local'])
            print("Mota: ",entrenamendua['type'])
            print("Ikusgarritasuna: ",entrenamendua['visibility'])
            print("Distantzia: ", entrenamendua['distance'])
            print("Batazbesteko abiadura: ", entrenamendua['average_speed'])
            print("Abiadura maximoa: ",entrenamendua['max_speed'])
            print("Pultsometroa: ",entrenamendua['has_heartrate'])
            print("-------------------------------------------------")

def getActivitiesID():
    print(stravaApiKud.getAthlete())
    parametroak={}
    em = stravaApiKud.getActivities(parametroak)
    ac = stravaApiKud.getActivityId(em[0]["id"])
    print(ac["name"], ac["type"], ac["distance"])



if __name__ == '__main__':
    stravaApiKud.getAccessToTheAPI()
    getActivities()
    getActivitiesID()

    
