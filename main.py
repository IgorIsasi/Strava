from Bista.ongiEtorri import OngiEtorri
#from view.main import Leihoa
from controllers.DBKudeatzailea.DBKud import kudeatzaile
#import mysql.connector

def main():
    if __name__ == '__main__':
        l=OngiEtorri()
        
        #kud = DBKud.DBKudeatzailea()
        #kud.kargatuDB()
        #l=Leihoa()          
           
        kudeatzaile.kargatuDB()

main()