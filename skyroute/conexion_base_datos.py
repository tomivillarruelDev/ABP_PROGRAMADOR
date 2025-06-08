# conexion_base_datos.py
# Conexión y operaciones con MySQL

import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Aquí se implementarán las funciones de conexión y operaciones con la base de datos

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        
        if conexion.is_connected():
            print("Conexión a la base de datos establecida correctamente.")
            
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def cerrar_conexion(conexion):
    if conexion:
        conexion.close()
