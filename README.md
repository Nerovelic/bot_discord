# Bot de Discord para Servidor de Minecraft

Este bot de Discord permite administrar fácilmente un servidor de Minecraft con una serie de comandos. A continuación se detallan los comandos disponibles y su funcionamiento.

## Comandos disponibles

- **`status`**: Muestra si el servidor de Minecraft está abierto o cerrado.
  - **Uso**: `/status`
  - **Descripción**: Este comando te informa sobre el estado actual del servidor, indicando si está en funcionamiento o detenido.

- **`time`**: Muestra los días que el servidor está abierto y cerrado.
  - **Uso**: `/time`
  - **Descripción**: Utiliza este comando para obtener un registro de los días en que el servidor ha estado operativo o cerrado.

- **`start`**: Sirve para abrir o iniciar el servidor. (no disponible en la nube)
  - **Uso**: `/start`
  - **Descripción**: Este comando permite iniciar el servidor de Minecraft, poniéndolo en línea para que los jugadores puedan conectarse.

- **`help`**: Muestra esta lista de comandos.
  - **Uso**: `/help`
  - **Descripción**: Este comando muestra una lista de todos los comandos disponibles y sus descripciones, proporcionando una referencia rápida para los usuarios.

<details>
  <summary> Comandos ocultos</summary>

  - **`stop`**: Sirve para detener o cerrar el server. (no disponible en la nube)
  - **Uso**: `.stop`
  - **Descripción**: Este commando lo que hace es detener o cerrar el server de minecraft de manera segura.

- **`tiempo`**: Muestra el tiempo de actividad del servidor de Minecraft.
  - **Uso**: `.tiempo`
  - **Descripción**: Utiliza este comando para obtener información sobre el tiempo total que el servidor ha estado en funcionamiento desde su última puesta en marcha.

- **`sincronizar`**: Sincroniza el bot de discord con la pc.
  - **Uso**: `.sincronizar`
  - **Descripción**: Este comando se utiliza para sincronizar los comandos / con el bot de pc.
    
- **`nuke`**: Le hace kick a todos los jugadores del servidor. (no disponible en la nube)
  - **Uso**: `.nuke`
  - **Descripción**: Este commando hace kick a los jugadores del servidores.

</details>

## Instalación y Configuración

Para utilizar este bot en tu servidor de Discord, sigue estos pasos:

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/Nerovelic/bot_discord.git
    ```

2. **Instalar dependencias**:
    ```bash
    cd bot_discord
    ```
   **Instalar discord.py**:
   ```bash
    pip install discord.py
    ```
   **Instalar psutil**:
   ```bash
    pip install psutil
    ```
   **Instalar pytz**:
   ```bash
    pip install pytz
    ```
    **Instalar unidecode**:
   ```bash
    pip install unidecode
    ```
   **Instalar python-dotenv**:
   ```bash
    pip install python-dotenv
    ```
   **Instalar requests**:
   ```bash
    pip install requests
    ```

3. **Configurar el bot**:
    - Crea el archivo `.env` e edítalo para agregar tu token de Discord y GUILD_ID de tu grupo de discord para que el bot funcione.

4. **Iniciar el bot**:
    ```bash
    py o python bot.py
    ```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar, por favor realiza un fork del repositorio y crea una nueva rama para tus modificaciones. Luego, envía un pull request con una descripción detallada de los cambios.

---

Desarrollado por [Nerovelic](https://github.com/Nerovelic)
