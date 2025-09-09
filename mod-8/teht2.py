import mysql.connector

def get_airport_count(country_code):
    sql = f"SELECT type, count(*) FROM airport where iso_country='{country_code}' group by type"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Kenttiä, joiden tyyppi on {row[0]} on {row[1]}.")
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

country_code = input("Anna maakoodi: ")
get_airport_count(country_code)
