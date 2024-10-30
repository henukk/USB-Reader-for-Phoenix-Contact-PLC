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
