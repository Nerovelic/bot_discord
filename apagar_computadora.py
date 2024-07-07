import os
import time
import subprocess
from datetime import datetime, timedelta
import pytz

# Configurar la zona horaria de Tijuana
tijuana_tz = pytz.timezone('America/Tijuana')

def run_shutdown_logic():
    # Obtener la hora actual en la zona horaria de Tijuana
    now = datetime.now(tijuana_tz)
    
    # Imprimir la fecha y hora actuales
    print(f"Fecha y hora actuales en Tijuana: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # Comprobar si hoy es miércoles y son las 12:00 AM
    if now.weekday() == 2:
        # Obtener el próximo miércoles a las 12:00 AM
        next_wednesday = now + timedelta(days=(2 - now.weekday() + 7) % 7)
        next_wednesday = next_wednesday.replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Calcular el tiempo en segundos hasta el próximo miércoles a las 12:00 AM
        time_until_shutdown = (next_wednesday - now).total_seconds()

        # Esperar 1 minuto (60 segundos) antes de ejecutar el script cerrado_server.py
        time.sleep(60)

        # Ejecutar el script cerrado_server.py
        subprocess.Popen(["python", "C:\\Users\\pc\\Desktop\\bot_discord\\cerrado_server.py"])

        # Esperar 12 minutos (720 segundos)
        time.sleep(720)

        # Programar el apagado
        os.system(f'shutdown /s /t {int(time_until_shutdown)}')
        print(f"Computadora se apagará en {int(time_until_shutdown)} segundos.")
    else:
        print("Esperando hasta el próximo miércoles a las 12:00 AM...")

# Bucle principal para mantener el script activo y revisar periódicamente cada 5 horas
while True:
    run_shutdown_logic()
    # Esperar 5 horas antes de revisar de nuevo
    time.sleep(5 * 3600)  # 5 horas en segundos

