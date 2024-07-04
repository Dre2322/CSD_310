import mysql.connector
from mysql.connector import Error

def show_films(cursor, title):
    query = """
    SELECT film_name AS Name, 
           director AS Director, 
           genre_name AS Genre, 
           studio_name AS 'Studio Name' 
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    films = cursor.fetchall()
    
    print("\n-- {} --".format(title))
    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre: {}".format(film[2]))
        print("Studio Name: {}".format(film[3]))
        print()

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
        
        # Display films before any changes
        show_films(cursor, "DISPLAYING FILMS")
        
        # Insert a new film
        insert_query = """
        INSERT INTO film (film_name, studio_id, genre_id, runtime, director)
        VALUES ('Star Wars', 1, 2, 121, 'George Lucas')
        """
        cursor.execute(insert_query)
        connection.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
        
        # Update the genre of the film Alien to Horror
        update_query = """
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien'
        """
        cursor.execute(update_query)
        connection.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")
        
        # Delete the film Gladiator
        delete_query = """
        DELETE FROM film
        WHERE film_name = 'Gladiator'
        """
        cursor.execute(delete_query)
        connection.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
