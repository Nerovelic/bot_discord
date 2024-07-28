import pyautogui
import time
import subprocess

def countdown_and_shutdown():
    # Anuncio de que el servidor se cerrará en 10 minutos
    pyautogui.write('say El servidor se va cerrar en 10 minutos')
    pyautogui.press('enter')
    
    # Espera 5 minutos
    time.sleep(300)  # 300 segundos = 5 minutos
    
    # Anuncio de que el servidor se cerrará en 5 minutos
    pyautogui.write('say El servidor se va cerrar en 5 minutos')
    pyautogui.press('enter')
    
    # Espera otros 4 minutos
    time.sleep(240)  # 240 segundos = 4 minutos

    # Anuncio de que el servidor se cerrará en 1 minuto
    pyautogui.write('say El servidor se va cerrar en 1 minuto')
    pyautogui.press('enter')

    # Cuenta regresiva de 1 minuto con mensajes específicos
    countdown_messages = [
        "Quedan 45 segundos para cerrar el servidor.",
        "Quedan 30 segundos para cerrar el servidor.",
        "Quedan 15 segundos para cerrar el servidor.",
        "Quedan 5 segundos para cerrar el servidor.",
        "Deteniendo el servidor..."
    ]

    intervals = [15, 15, 15, 10] 

    for message, interval in zip(countdown_messages, intervals):
        pyautogui.write(f'say {message}')
        pyautogui.press('enter')
        print(message)  # Para verificar en la consola
        time.sleep(interval)
    
    # Aquí agregas el código necesario para detener el servidor
    time.sleep(5)

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
countdown_and_shutdown()
