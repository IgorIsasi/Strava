from controllers.StravaAPI import stravaApiKud


if __name__ == '__main__':
    stravaApiKud.getAccessToTheAPI()
    print(stravaApiKud.getAthlete())
    em = stravaApiKud.getActivities()
    ac = stravaApiKud.getActivityId(em[0]["id"])
    print(ac["name"], ac["type"], ac["distance"])
    astr = stravaApiKud.getActivityStreams(em[0]["id"])
    print(astr)