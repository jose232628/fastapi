import mysql.connector

# Configuración de la conexión
database = mysql.connector.connect(
    host = 'localhost',   # O la IP de tu contenedor Docker si usas "docker inspect"
    port = 3307,
    ssl_disabled  = True,      # Puerto por defecto de MySQL
    user = 'root',        # Usuario de MySQL
    password = 'strong_password',  # La contraseña que configuraste
    database = 'tabla_prueba'    # Puedes cambiarlo al nombre de tu base de datos
)