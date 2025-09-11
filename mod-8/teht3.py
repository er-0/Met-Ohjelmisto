import mysql.connector
from geopy import distance

def get_airport_distance(ident1, ident2):
    sql = f"SELECT latitude_deg,longitude_deg FROM airport where ident='{ident1}' or ident='{ident2}'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 2 :
        location1, location2 = result
        calc_distance = distance.distance(location1, location2).km
        print(f"Kenttien etäisyys on {calc_distance:0.0f} kilometriä.")
    return

# main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='elina',
         password='mielikuva',
         autocommit=True
         )

ident1 = input("Anna ensimmäinen ICAO-koodi: ")
ident2 = input("Anna toinen ICAO-koodi: ")
get_airport_distance(ident1, ident2)

connection.close()