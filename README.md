# USB Reader for Phoenix Contact PLC

Este repositorio contiene un ejemplo de cómo leer eventos de dispositivos USB (como teclados y lectores de códigos de barras) conectados a un PLC Phoenix Contact EPC 1502 utilizando Yocto Linux Kirkstone. Se utiliza un script en Python que se ejecuta desde Node-RED para interpretar los eventos del puerto USB.

> ℹ️ **Nota**: Este proyecto está diseñado y probado específicamente para el PLC Phoenix Contact EPC 1502 con Yocto Linux Kirkstone. Puede requerir ajustes para otros modelos o sistemas.

## Tabla de Contenidos
- [Introducción](#introducción)
- [Contenido del repositorio](#contenido-del-repositorio)
- [Instalación](#instalación)
  - [Configuración del Entorno](#configuración-del-entorno)
  - [Preparación del Script en Python](#preparación-del-script-en-python)
  - [Modificación de Node-RED](#modificación-de-node-red)
- [Uso del Proyecto](#uso-del-proyecto)
- [Programa en Node-RED](#programa-en-node-red)
  - [Ejemplo de Uso del Flujo](#ejemplo-de-uso-del-flujo)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Introducción
El objetivo de este ejemplo es demostrar cómo leer e interpretar los eventos generados por dispositivos USB conectados al PLC, como un teclado o un lector de códigos de barras, en un entorno Node-RED.

## Contenido del Repositorio

La estructura del repositorio es la siguiente:

```plaintext
usb-plc-reader/
├── src/
│   └── [usbdrivers.py](/src/usbdrivers.py)              # Script en Python para leer eventos del puerto USB
├── flows/
│   └── [flows_usb.json](/flows/flows_usb.json)                # Flujos para importar en Node-RED
├── docs/
│   └── [setup_instructions.md](/docs/setup_instructions.md)        # Instrucciones adicionales de configuración
|   └── [how_it_works.md](/docs/how_it_works.md)              # Documentación del script de python
|   └── [examples.md](/docs/examples.md)                  # Ejemplos lectura USB
└── [README.md](/README.md)                        # Documentación principal del proyecto
```

- [src/usbdrivers.py](src/usbdrivers.py): Script en Python para leer y decodificar eventos de dispositivos USB conectados.
- [flows/flows_usb.json](flows/flows_usb.json): Flujos Node-RED necesarios para ejecutar el script desde el PLC.
- [docs/setup_instructions.md](docs/setup_instructions.md): Instrucciones detalladas de configuración y pasos adicionales opcionales.
- [docs/how_it_works.md](docs/how_it_works.md): Explicación del funcionamiento del script de Python.
- [docs/examples.md](docs/examples.md): Ejemplos prácticos de uso para la lectura de dispositivos USB.


## Instalación

### Configuración del Entorno
1. **Configurar acceso root:**
   - Crear nueva contraseña para el usuario `root` en el dispositivo:
     ```bash
     sudo passwd root
     ```
> ⚠️ **Advertencia**: Cambiar la contraseña de root es una operación sensible; asegúrate de recordar la nueva contraseña para evitar problemas de acceso al dispositivo.

### Preparación del Script en Python
1. Crear un directorio para el script:
   ```bash
   mkdir /home/root/usbdrivers
   ```
2. Crear el archivo `usbdrivers.py`:
   ```bash
   touch /home/root/usbdrivers/usbdrivers.py
   ```
3. Copiar el código Python del archivo [src/usbdrivers.py](src/usbdrivers.py) de este repositorio al archivo `usbdrivers.py` en el dispositivo:
   ```bash
   nano /home/root/usbdrivers/usbdrivers.py
   ```
   (Pegar el contenido y guardar).

### Modificación de Node-RED
1. Abrir el archivo de configuración de Node-RED:
   ```bash
   nano /opt/plcnext/appshome/data/60002172000551/docker-compose.yml
   ```

> ℹ️ **Nota**: El directorio `60002172000551` puede variar según la versión de Node-RED instalada; consulta la estructura de archivos en el dispositivo si es necesario.
   
2. Modificar el archivo de la siguiente manera:
   ```yaml
   version: "3.7"
   services:
     node-red:
       image: ${IMAGE_NAME}:${IMAGE_TAG}
       ports:
         - 51880:1880
       user: root
       volumes:
         - ./volumes/node-red:/data
         - /home/root/usbdrivers:/usbdrivers
       restart: unless-stopped
       privileged: true
   ```

> ❗ **Importante**: Verifica que la ruta `/home/root/usbdrivers` esté correctamente escrita y montada. Los permisos incorrectos pueden impedir la lectura de eventos USB.


3. Reiniciar el dispositivo para aplicar los cambios:
   ```bash
   reboot
   ```

### Programa en Node-RED
1. Abrir el editor de Node-RED.
2. Importar el archivo de flujo [`flows/flows_usb.json`](flows/flows_usb.json) de este repositorio.

## Uso del Proyecto
Con Node-RED configurado para utilizar el script Python, se puede conectar un teclado o lector de código de barras al PLC y observar cómo se interpretan los eventos en tiempo real. 

> ✅ **Tip**: Conecta y prueba el dispositivo USB (teclado o lector de código de barras) antes de comenzar. Puedes verificar la salida de eventos USB en Node-RED para asegurarte de que el script está funcionando.

## Programa en Node-RED

El archivo [`flows/flows_usb.json`](flows/flows_usb.json) contiene un flujo de Node-RED que ejecuta el script `usbdrivers.py` en Python para leer eventos desde dispositivos USB conectados al PLC Phoenix Contact. Cada nodo `exec` en el flujo ejecuta el script en un puerto USB específico y muestra los resultados en un nodo `debug` de Node-RED.

#### Nodos Principales en `flows_usb.json`

- **Nodo Inject ("Read driver 1")**: Este nodo de inyección permite iniciar manualmente el flujo para ejecutar el script `usbdrivers.py`. La configuración actual está preparada para leer eventos desde `/dev/input/event3` y `/dev/input/event4`.

- **Nodo Exec (Ejecutar Script Python)**: El nodo `exec` ejecuta el comando `python3 /usbdrivers/usbdrivers.py <EventNumber>`. Los números de evento `3` y `4` especifican qué puerto de entrada (`/dev/input/eventX`) se va a leer. Estos valores pueden ajustarse según el puerto USB específico de los dispositivos conectados.

- **Nodo Debug**: El nodo `debug` muestra la salida generada por el script en la consola de depuración de Node-RED. Esto permite visualizar en tiempo real los eventos detectados por los dispositivos USB conectados.

### Ejemplo de Uso del Flujo

1. **Ejecutar el Flujo**: Abre Node-RED y ubica el flujo importado.
2. **Iniciar Lectura de Eventos**: Haz clic en el nodo `Inject` etiquetado como "Read driver 1" para iniciar la lectura de eventos en el dispositivo USB conectado.
3. **Ver la Salida**: La salida de los eventos USB se mostrará en el nodo `Debug` de Node-RED, donde se podrá observar el texto capturado en tiempo real, como entradas de teclado o datos de escaneo.

> ⚠️ **Nota**: Los puertos `/dev/input/eventX` pueden variar según el dispositivo USB conectado y la configuración del sistema. Asegúrate de verificar el puerto asignado al dispositivo conectado, especialmente si hay varios dispositivos USB conectados al PLC.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este repositorio, por favor sigue los siguientes pasos:
1. Crea un _fork_ de este repositorio.
2. Haz tus cambios en una nueva rama.
3. Envía un _pull request_ con una descripción detallada de tus cambios.

> 💡 **Tip**: Antes de enviar un _pull request_, prueba tus cambios en un entorno seguro para evitar afectar configuraciones críticas del PLC.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
