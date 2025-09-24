# db.py
import mysql.connector

# Create a connection object
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='school_project',
    user='elina',
    password='mielikuva',
    autocommit=True
)