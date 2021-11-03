from controllers.StravaAPI import stravaApiKud
import datetime
import time

if __name__ == '__main__':
    stravaApiKud.getAccessToTheAPI()
    print(stravaApiKud.getAthlete())

    today = datetime.datetime.today()
    yesterday=today-datetime.timedelta(days=1) 
    yesterday=yesterday.timestamp() #Atzoko timestamp
    parametroak={'after':yesterday, 'per_page':3}# 'before':50, 'page':1, 'per_page':5}
    print(stravaApiKud.getActivities(parametroak))

