import pyautogui
import time
import subprocess

def shutdown():
    # Anuncio de que el servidor se cerrarásay El servidor se 
    pyautogui.write('say Deteniendo el servidor...')
    pyautogui.press('enter')

    # Aquí agregas el código necesario para detener el servidor
    time.sleep(5)

    pyautogui.write('stop')
    pyautogui.press('enter')

    # Comando de cmd para cerrar la ventana actual
    command = 'taskkill /IM cmd.exe /F'

    # Ejecutar el comando de cmd
    subprocess.run(command, shell=True)

# Llamar a la función de cuenta regresiva y cierre del servidor
shutdown()
