import mysql.connector
from mysql.connector import Error

# Add the database configuration object with your user and password
config = {
    'user': 'root',
    'password': 'Dopestylo23!',
    'host': '127.0.0.1',
    'database': 'movies'
}

# Add the connection test code to mysql_test.py
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
