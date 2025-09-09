import mysql.connector

def get_airport(ident):
    sql = f"SELECT name, municipality FROM airport where ident='{ident}'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Kenttä {row[0]} sijaitsee kunnassa {row[1]}.")
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

ident = input("Anna ICAO-koodi: ")
get_airport(ident)
