import pyautogui
import time
import subprocess

# Anuncio de que el servidor se cerrará en 10 minutos
pyautogui.write('say El servidor se va cerrar en 10 minutos')
pyautogui.press('enter')

# Espera 5 minutos
time.sleep(300)  # 300 segundos = 5 minutos

# Anuncio de que el servidor se cerrará en 5 minutos
pyautogui.write('say El servidor se va cerrar en 5 minutos')
pyautogui.press('enter')
    
# Espera otros 5 minutos
time.sleep(300)  # 300 segundos = 5 minutos

# Anuncio de que el servidor se cerrarásay El servidor se 
pyautogui.write('say Deteniendo el servidor...')
pyautogui.press('enter')

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