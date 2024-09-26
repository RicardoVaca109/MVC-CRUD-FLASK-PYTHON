import mysql.connector
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Conexión a la base de datos utilizando las variables de entorno
conexion_database = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),  # Revisa que tu contraseña esté correctamente establecida
    database=os.getenv('DB_NAME') 
)
