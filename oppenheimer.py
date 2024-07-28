import pyautogui
import time
import subprocess

def shutdown_server():
    # Kick a todos los jugadores
    pyautogui.write('say El servidor se va a cerrar porque activaron el NUKE')
    pyautogui.press('enter')

    # Kick a todos los jugadores
    pyautogui.write('kick @a')
    pyautogui.press('enter')

    # Esperar antes de detener el servidor
    time.sleep(5)

    # Comandos para detener el servidor
    pyautogui.write('stop')
    pyautogui.press('enter')

    # Comando de cmd para cerrar la ventana actual 
    command = 'taskkill /IM cmd.exe /F'

    # Ejecutar el comando de cmd
    subprocess.run(command, shell=True)

# Llamar a la función de cierre del servidor
shutdown_server()
