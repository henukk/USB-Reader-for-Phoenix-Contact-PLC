# Instrucciones de Configuración Adicionales

Este archivo cubre configuraciones avanzadas y ajustes opcionales que pueden ser necesarios en ciertas configuraciones de hardware o software.

## Requisitos de Sistema
- **Hardware**: Este proyecto ha sido probado en un PLC Phoenix Contact EPC 1502.
- **Sistema Operativo**: Yocto Linux Kirkstone.
- **Software Necesario**:
  - Node-RED versión 4.0.2.1 o superior, instalado en PLCnext Store.
  - Python 3.x instalado en el sistema.

## Configuración Opcional

1. **Modificar el Script para Otros Eventos**:
   - La configuración actual del script está diseñada para interpretar entradas de teclado y códigos de barras. Para adaptarlo a otros dispositivos USB, modifica el archivo `usbdrivers.py` en la sección `key_map` con el código de los eventos específicos del dispositivo.

2. **Uso de Otros Directorios de Instalación**:
   - Si prefieres ubicar el script en otro directorio, asegúrate de ajustar el archivo `docker-compose.yml` de Node-RED para reflejar la ruta correcta.

3. **Configuración de Permisos en Node-RED**:
   - Si enfrentas problemas de permisos al leer `/dev/input/eventX`, verifica que el usuario de Node-RED tenga acceso a los dispositivos de entrada. Puede ser necesario añadir permisos adicionales a `/dev/input` en el archivo `docker-compose.yml`.

4. **Configuración para Diferentes PLCs**:
   - Si estás utilizando un PLC distinto, asegúrate de revisar la configuración de Node-RED y de adaptar los flujos a la arquitectura del nuevo dispositivo.

## Solución de Problemas Comunes

1. **Node-RED no detecta el script de Python**:
   - Verifica que la ruta a `usbdrivers.py` esté correctamente montada en el archivo `docker-compose.yml`.

2. **Permisos de Lectura de Eventos USB**:
   - Es posible que algunos eventos de `/dev/input` requieran permisos de superusuario. Añade `privileged: true` en `docker-compose.yml` para asegurarte de que Node-RED tenga los permisos necesarios.

Para preguntas adicionales, consulta la [documentación oficial de Node-RED](https://nodered.org/docs/) o la [documentación de PLCnext](https://www.plcnext-community.net/).
