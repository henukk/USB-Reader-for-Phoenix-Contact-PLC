# Cómo Funciona el Código

Este documento describe cómo el script `usbdrivers.py` interpreta eventos del puerto USB en el PLC Phoenix Contact EPC 1502.

## Flujo General del Código

1. **Lectura del Evento**:
   - El script abre el archivo `/dev/input/eventX`, donde `X` representa el número del evento USB asignado al dispositivo.
   - Lee paquetes de 24 bytes que contienen información sobre el evento (timestamp, tipo, código y valor).

2. **Interpretación del Evento**:
   - Los eventos de tipo `1` (evento de botón) con un valor `1` (presionado) representan pulsaciones de teclas.
   - El script convierte el código de tecla (`code`) usando el diccionario `key_map` para traducirlo a caracteres legibles.

3. **Buffer y Envío de Datos**:
   - Los caracteres se almacenan en un buffer temporal.
   - Cuando el código detecta la tecla Enter (código `28`), imprime el contenido del buffer y lo vacía para la siguiente secuencia de entrada.

## Diccionario de Traducción (key_map)
El diccionario `key_map` se usa para mapear códigos de teclas numéricas a caracteres específicos. Este mapeo es necesario para convertir los eventos USB en texto legible por humanos. Puedes modificar `key_map` para añadir o cambiar teclas según el dispositivo conectado.

## Errores Comunes y Solución
- **Código desconocido**: Si se recibe un código que no está en `key_map`, el script simplemente lo ignora, asegurando que solo los caracteres conocidos se procesen.
- **Tecla Enter**: El código `28` es clave, ya que indica el final de una secuencia de entrada (usado aquí como el botón Enter).

## Integración con Node-RED

Node-RED se utiliza para ejecutar el script `usbdrivers.py` y mostrar los datos de eventos USB capturados en tiempo real. La integración con Node-RED se realiza mediante un flujo que ejecuta el script en un entorno de PLC.

### Descripción del Flujo de Node-RED

1. **Nodo Inject**: Inicia el flujo para ejecutar el script manualmente y permite leer eventos en el dispositivo conectado (por ejemplo, teclado o lector de códigos de barras).
   
2. **Nodo Exec**: Ejecuta el script `usbdrivers.py` en el PLC mediante el comando:
   ```bash
   python3 /usbdrivers/usbdrivers.py <EventNumber>```
   - `<EventNumber>` representa el número de evento del puerto USB (por ejemplo, `3` o `4`).
   - Este nodo ejecuta el script y permite leer el archivo `/dev/input/eventX` para capturar los eventos USB.

3. **Nodo Debug**: Muestra la salida del script en la consola de depuración de Node-RED. La salida incluye los caracteres o datos capturados desde el dispositivo USB, como entradas de teclado o escaneos de códigos de barras.

### Cómo Node-RED Interactúa con el Script

El flujo de Node-RED ejecuta el script y espera los datos capturados, mostrándolos en tiempo real en el nodo `Debug`. Esto permite observar y verificar fácilmente las entradas capturadas sin necesidad de abrir la terminal en el PLC.

> 💡 **Tip**: Puedes ajustar el número de evento `<EventNumber>` en el flujo de Node-RED si el dispositivo está asignado a un puerto diferente.
