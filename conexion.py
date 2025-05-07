import mysql.connector
from datetime import datetime

def insertar_mensaje(original, cifrado):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="taeMoon04", 
            database="cifrados"
        )

        cursor = conexion.cursor()
        query = "INSERT INTO mensajes (mensaje_original, mensaje_cifrado, fecha_cifrado) VALUES (%s, %s, %s)"
        valores = (original, cifrado, datetime.now())
        cursor.execute(query, valores)
        conexion.commit()

        print("Mensaje insertado correctamente.")
    except mysql.connector.Error as err:
        print("Error al insertar:", err)
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()