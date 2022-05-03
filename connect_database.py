import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="youtube_database"
)

print("Connected to:", db.get_server_info())

if db.is_connected():
        db_Info = db.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)