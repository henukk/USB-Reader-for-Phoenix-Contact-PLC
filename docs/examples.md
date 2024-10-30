# Ejemplos de Uso

Esta guía proporciona ejemplos prácticos para conectar y leer dispositivos USB en el PLC Phoenix Contact.

## Ejemplo 1: Lectura de Teclado USB

1. Conecta un teclado USB al puerto USB del PLC.
2. Asegúrate de que el script `usbdrivers.py` esté en ejecución y vinculado al archivo de evento correcto (por ejemplo, `/dev/input/event0`).
3. Abre Node-RED y visualiza la salida en el nodo de depuración.

### Ejemplo de Salida Esperada

Al presionar la tecla `H`, `O`, `L`, `A`, y luego Enter en el teclado USB, la salida esperada será:

``` HOLA ```

## Ejemplo 2: Lector de Código de Barras

1. Conecta el lector de código de barras USB.
2. Escanea un código de barras, y el dispositivo debería enviar una serie de eventos USB.
3. El script interpretará estos eventos y mostrará el código escaneado en Node-RED.

### Ejemplo de Salida

Escanear un código de barras podría generar una salida similar a esta:

```1234567890123```

Asegúrate de que el lector esté configurado para enviar un código de "Enter" después de cada escaneo, lo cual activará el envío de los datos a Node-RED.
