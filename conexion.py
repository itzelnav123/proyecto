import mysql.connector

def conectar_asistencia():

    try:

        return mysql.connector.connect(

            host="localhost",

            user="root",

            password="",

            database="asistencia",

            port=3306

        )

    except mysql.connector.Error as error:

        print("Error:", error)

        return None