from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector

# Crear la instancia de la aplicación
app = FastAPI()

# Configurar directorios para plantillas y archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Ruta principal: Inicio
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Inicio"})

# Ruta Menú
@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request, "title": "Menú"})

# Ruta Reservas
@app.get("/reservas", response_class=HTMLResponse)
async def reservas(request: Request):
    return templates.TemplateResponse("reservas.html", {"request": request, "title": "Reservas"})

# Ruta Contacto
@app.get("/contacto", response_class=HTMLResponse)
async def contacto(request: Request):
    return templates.TemplateResponse("contacto.html", {"request": request, "title": "Contacto"})

@app.get("/testdb")
async def test_db_connection():
    try:
        # Conectar a la base de datos MySQL
        connection = mysql.connector.connect(
            host="localhost",  # Cambia a la IP o nombre del host si no está en localhost
            user="root",       # Tu nombre de usuario de MySQL
            password="strong_password",  # Tu contraseña de MySQL
            database="tu_base_de_datos"  # Nombre de la base de datos que quieres conectar
        )
        
        # Ejecutar una consulta para verificar la conexión
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")  # Consultar la base de datos actual
        result = cursor.fetchone()
        
        cursor.close()  # Cierra el cursor
        connection.close()  # Cierra la conexión
        
        # Responde con el nombre de la base de datos a la que se ha conectado
        return {"message": f"Conectado correctamente a la base de datos: {result[0]}"}
    except mysql.connector.Error as err:
        # Si ocurre un error, responder con un error
        return {"error": f"No se pudo conectar a la base de datos: {err}"}