import discord
from discord.ext import commands,tasks
import psutil
from datetime import datetime
import pytz
import os
import asyncio
from unidecode import unidecode
from dotenv import load_dotenv
import requests
import logging
from google.cloud import logging as cloud_logging

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración del bot
TOKEN = os.getenv('TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

# Set up Google Cloud logging
cloud_logging_client = cloud_logging.Client()
cloud_logging_client.setup_logging()

# Configure logging
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
intents.typing = True
intents.presences = True
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

# Define la zona horaria de Baja California (UTC-8:00)
baja_california_tz = pytz.timezone('America/Tijuana')

# Días de apertura y cierre
dias_cerrados = {"miércoles", "jueves"}
dias_abiertos = {"lunes", "martes", "viernes", "sábado", "domingo"}

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    check_internet.start()  # Iniciar el bucle de comprobación de Internet
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    
# Función para verificar si hay algún proceso de PowerShell en ejecución
def is_process_running():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if "powershell" in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Función para verificar la conexión a Internet
def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Tarea para comprobar periódicamente la conexión a Internet
@tasks.loop(seconds=10)  # Comprobar cada 10 segundos
async def check_internet():
    if not check_internet_connection():
        print("No internet connection. Attempting to reconnect...")
        await bot.logout()
        while not check_internet_connection():
            await asyncio.sleep(5)  # Espere 5 segundos antes de volver a comprobar
        print("Internet connection restored. Reconnecting...")
        await bot.login(TOKEN)
        await bot.connect()

# Función para verificar si el servidor está abierto o cerrado
def is_server_open():
    now = datetime.now(baja_california_tz)
    day_name = now.strftime("%A").lower()
    dias_semana = {
        "monday": "lunes",
        "tuesday": "martes",
        "wednesday": "miércoles",
        "thursday": "jueves",
        "friday": "viernes",
        "saturday": "sábado",
        "sunday": "domingo"
    }
    day_name_es = dias_semana[day_name]
    return day_name_es  in dias_abiertos

# Comando /status
@bot.tree.command(name="status", description="Muestra si el servidor de Minecraft está abierto o cerrado")
async def status(interaction: discord.Interaction):
    if is_server_open() and is_process_running():
        await interaction.response.send_message(f"El servidor de Minecraft está abierto, {interaction.user.mention}.")
    elif is_server_open() and not is_process_running():
        await interaction.response.send_message(f"El servidor de Minecraft no está disponible, {interaction.user.mention}.")
    else:
        await interaction.response.send_message(f"El servidor de Minecraft está cerrado, {interaction.user.mention}.")

# Comando /time
@bot.tree.command(name="time", description="Muestra los días que el servidor está abierto y cerrado")
async def time(interaction: discord.Interaction):
    open_days = "lunes a domingo a las 12 AM"
    closed_days = "miércoles y jueves a las 12 AM"
    
    await interaction.response.send_message(f"Días abiertos: {open_days}\nDías cerrados: {closed_days}")

# Comando /help
@bot.tree.command(name="help", description="Muestra la lista de comandos del bot")
async def help_command(interaction: discord.Interaction):
    help_message = (
        "Comandos disponibles:\n"
        "status - Muestra si el servidor de Minecraft está abierto o cerrado.\n"
        "time - Muestra los días que el servidor está abierto y cerrado.\n"
        "start - Sirve para abrir o iniciar el server.\n"
        "help - Muestra esta lista de comandos."
    )
    await interaction.response.send_message(help_message)

# Comando /start
@bot.tree.command(name="start", description="Inicia el proceso de PowerShell si no hay ninguno en ejecución")
async def start(interaction: discord.Interaction):
    await interaction.response.send_message("El comando no está disponible")

# Evento para detectar mensajes y responder con el estado del servidor
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Frases clave para verificar el estado del servidor
    frases_clave = [
        "el server está abierto?",
        "el server esta abierto?",
        "está abierto el server?",
        "esta abierto el server?",
        "el server de minecraft está abierto?",
        "el server de minecraft esta abierto?",
        "el servidor está abierto?",
        "el servidor esta abierto?",
        "el servidor de minecraft está abierto?",
        "el servidor de minecraft esta abierto?",
        "está abierto el servidor?",
        "esta abierto el servidor?"
    ]

    # Convertir el mensaje a minúsculas para facilitar la comparación
    contenido_mensaje = message.content.lower()

    if any(frase in contenido_mensaje for frase in frases_clave) or any(unidecode(frase) in unidecode(contenido_mensaje) for frase in frases_clave):
        server_open = is_server_open()
        process_running = is_process_running()
        if server_open and process_running:
            await message.channel.send(f"El servidor de Minecraft está abierto, {message.author.mention}.")
        elif server_open and not process_running:
            await message.channel.send(f"El servidor de Minecraft no está disponible, {message.author.mention}.")
        else:
            await message.channel.send(f"El servidor de Minecraft está cerrado, {message.author.mention}.")
    
    await bot.process_commands(message)

# Comando con prefijo para cerrar el servidor (stop)
@bot.command(name="stop", description="Sirve para detener o cerrar el server")
async def stop(ctx):
    await ctx.send("El comando no está disponible")

# Comando de sincronización con prefijo
@bot.command(name="sincronizar", description="Sincroniza el bot")
async def sincronizar(ctx):
    await ctx.send("Listo!")
    await ctx.send("Comandos slash sincronizados.")

# Comando con prefijo para ver la hora
@bot.command(name="tiempo", description="Muestra el día actual y la hora")
async def tiempo(ctx):
    now = datetime.now(baja_california_tz)
    
    # Días de la semana en español
    dias_semana = {
        "Monday": "lunes",
        "Tuesday": "martes",
        "Wednesday": "miércoles",
        "Thursday": "jueves",
        "Friday": "viernes",
        "Saturday": "sábado",
        "Sunday": "domingo"
    }
    
    # Obtener el nombre del día en español
    day_name = dias_semana[now.strftime("%A")]
    current_time = now.strftime("%H:%M:%S")  # Obtener la hora en formato HH:MM:SS
    
    # Construir el mensaje de respuesta
    response_message = f"Hoy es {day_name} y son las {current_time} UTC."
    
    await ctx.send(response_message)

# EE del servidor le hace kick a todos los jugadores
@bot.command(name="nuke", description="Le hace kick a todos los jugadores y se cierra el server")
async def nuke(ctx):
    await ctx.send("El comando no está disponible")

# Ejecutar el bot
bot.run(TOKEN)
