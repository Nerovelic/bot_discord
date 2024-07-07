# Bot de Discord para Servidor de Minecraft

Este bot de Discord permite administrar fácilmente un servidor de Minecraft con una serie de comandos. A continuación se detallan los comandos disponibles y su funcionamiento.

## Comandos disponibles

- **`status`**: Muestra si el servidor de Minecraft está abierto o cerrado.
  - **Uso**: `/status`
  - **Descripción**: Este comando te informa sobre el estado actual del servidor, indicando si está en funcionamiento o detenido.

- **`time`**: Muestra los días que el servidor está abierto y cerrado.
  - **Uso**: `/time`
  - **Descripción**: Utiliza este comando para obtener un registro de los días en que el servidor ha estado operativo o cerrado.

- **`start`**: Sirve para abrir o iniciar el servidor.
  - **Uso**: `/start`
  - **Descripción**: Este comando permite iniciar el servidor de Minecraft, poniéndolo en línea para que los jugadores puedan conectarse.

- **`stop`**: Sirve para detener o cerrar el servidor.
  - **Uso**: `/stop`
  - **Descripción**: Utiliza este comando para detener el servidor de Minecraft de manera segura, cerrándolo para evitar que los jugadores se conecten.

- **`help`**: Muestra esta lista de comandos.
  - **Uso**: `/help`
  - **Descripción**: Este comando muestra una lista de todos los comandos disponibles y sus descripciones, proporcionando una referencia rápida para los usuarios.

## Instalación y Configuración

Para utilizar este bot en tu servidor de Discord, sigue estos pasos:

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/Nerovelic/bot_discord.git
    ```

2. **Instalar dependencias**:
    ```bash
    cd bot_discord
    npm install
    ```

3. **Configurar el bot**:
    - Renombra el archivo `.env.example` a `.env` y edítalo para agregar tu token de Discord y otros detalles de configuración necesarios.

4. **Iniciar el bot**:
    ```bash
    npm start
    ```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar, por favor realiza un fork del repositorio y crea una nueva rama para tus modificaciones. Luego, envía un pull request con una descripción detallada de los cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

Desarrollado por [Nerovelic](https://github.com/Nerovelic)
