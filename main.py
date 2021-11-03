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
        r=stravaApiKud.getActivities(parametroak)
        print("-------------------------------------------------")
        for entrenamendua in r:
            print("Id: ", entrenamendua['id'])
            print("Izena: ",entrenamendua['name'])
            print("Data: ",entrenamendua['start_date_local'])
            print("Mota: ",entrenamendua['type'])
            print("Ikusgarritasuna: ",entrenamendua['visibility'])
            print("Distantzia: ", entrenamendua['distance'])
            print("Batazbesteko abiadura: ", entrenamendua['average_speed'])
            print("Abiadura maximoa: ",entrenamendua['max_speed'])
            print("Pultsometroa: ",entrenamendua['has_heartrate'])
            print("-------------------------------------------------")

            

def getActivitiesID(id):
    entrenamendua = stravaApiKud.getActivityId(id)
    print("Id: ", entrenamendua['id'])
    print("Izena: ",entrenamendua['name'])
    print("Data: ",entrenamendua['start_date_local'])
    print("Mota: ",entrenamendua['type'])
    print("Ikusgarritasuna: ",entrenamendua['visibility'])
    print("Distantzia: ", entrenamendua['distance'])
    print("Batazbesteko abiadura: ", entrenamendua['average_speed'])
    print("Abiadura maximoa: ",entrenamendua['max_speed'])
    print("Pultsometroa: ",entrenamendua['has_heartrate'])
    print("-------------------------------------------------")



def getActivitiesIDStream():



if __name__ == '__main__':
    stravaApiKud.getAccessToTheAPI()
    getAthlete()
    getActivities()
    getActivitiesID(6202857865)
    getActivitiesIDStreams()

    

