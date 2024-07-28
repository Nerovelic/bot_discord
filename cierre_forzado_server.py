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

    time.sleep(5)

    pyautogui.write('a')
    pyautogui.press('enter')

    time.sleep(5)

    # Comando de PowerShell para cerrar la ventana actual
    command = 'Stop-Process -Name "powershell"'

    # Ejecutar el comando de PowerShell
    subprocess.run(["powershell", "-Command", command], shell=True)

# Llamar a la función de cuenta regresiva y cierre del servidor
shutdown()
