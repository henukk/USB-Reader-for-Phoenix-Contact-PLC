Configuración root:
    Crear nueva contraseña para root
        - sudo passwd root

Preparación script python:
    Crear directorio en /home/root/
        - mkdir /home/root/usbdrivers

    Crear archivo python en /home/root/ llamado usbdrivers.py
        - touch /home/root/usbdrivers/usbdrivers.py

    Copiar codigo del archivo x a este nuevo archivo
        - nano /home/root/usbdrivers/usbdrivers.py

Modificar configuración node-red:
    Abrir archivo de configuración:
        - nano /opt/plcnext/appshome/data/60002172000551/docker-compose.yml
        (60002172000551 es el directorio para el directorio de Node-RED for PLCnext x86 version 4.0.2.1 de la PLCNext Stroe )
    Original:
        version: "3.7"
        services:
        node-red:
            image: ${IMAGE_NAME}:${IMAGE_TAG}
            ports:
            - 51880:1880
            user: ${USER_ID}
            volumes:
            - ./volumes/node-red:/data
            restart: unless-stopped
    Modificado:
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
    Reiniciar el dispositivo
        - reboot

Programa node red:
    Abrir el editor de node-red
    Importar el archivo flows_usb
