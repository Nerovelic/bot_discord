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

    time.sleep(5)

    pyautogui.write('a')
    pyautogui.press('enter')

    time.sleep(5)

    # Comando de PowerShell para cerrar la ventana actual
    command = 'Stop-Process -Name "powershell"'

    # Ejecutar el comando de PowerShell
    subprocess.run(["powershell", "-Command", command], shell=True)

# Llamar a la función de cierre del servidor
shutdown_server()
