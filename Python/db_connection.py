import mysql.connector
from mysql.connector import Error


def create_db_connection(host_name, user_name, user_password, db_name):
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='malav@7',
            database='car_rental_system'
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def close_db_connection(connection):
    """Close the database connection."""
    if connection:
        connection.close()
        print("MySQL connection is closed")
