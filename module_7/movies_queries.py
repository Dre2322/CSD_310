import mysql.connector
from mysql.connector import Error

config = {
    'user': 'root',
    'password': 'Dopestylo23!',  
    'host': '127.0.0.1',
    'database': 'movies'
}

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()

        # First Query: Select all fields from the studio table
        cursor.execute("SELECT * FROM studio;")
        studios = cursor.fetchall()
        print("-- DISPLAYING Studio RECORDS --")
        for studio in studios:
            print(f"Studio ID: {studio[0]}")
            print(f"Studio Name: {studio[1]}\n")

        # Second Query: Select all fields from the genre table
        cursor.execute("SELECT * FROM genre;")
        genres = cursor.fetchall()
        print("-- DISPLAYING Genre RECORDS --")
        for genre in genres:
            print(f"Genre ID: {genre[0]}")
            print(f"Genre Name: {genre[1]}\n")

        # Third Query: Select film names and runtime for films with runtime less than two hours
        cursor.execute("SELECT film_name, runtime FROM film WHERE runtime < 120;")
        short_films = cursor.fetchall()
        print("-- DISPLAYING Short Film RECORDS --")
        for film in short_films:
            print(f"Film Name: {film[0]}")
            print(f"Runtime: {film[1]}\n")

        # Fourth Query: Get a list of film names and directors grouped by director
        cursor.execute("SELECT film_name, director FROM film ORDER BY director;")
        directors_films = cursor.fetchall()
        print("-- DISPLAYING Director RECORDS in Order --")
        for record in directors_films:
            print(f"Film Name: {record[0]}")
            print(f"Director: {record[1]}\n")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
