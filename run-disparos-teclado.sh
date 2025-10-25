#!/bin/bash

# Script para instalar y ejecutar disparos-teclado
echo "Configurando disparos-teclado..."

# Verificar que estamos en el directorio correcto
if [ ! -f "main.py" ] || [ ! -d "sounds" ]; then
    echo "Error: Asegúrate de estar en el directorio ~/disparos-teclado y que main.py y la carpeta sounds/ existan."
    exit 1
fi

# Añadir usuario al grupo input (necesario para evdev)
if ! groups | grep -q input; then
    sudo usermod -a -G input $USER
    echo "Usuario añadido al grupo 'input'. Cierra sesión y vuelve a iniciarla, luego ejecuta este script de nuevo."
    exit 0
fi

# Actualizar e instalar dependencias del sistema
sudo apt update
sudo apt install -y ffmpeg python3-venv || { echo "Error instalando ffmpeg o python3-venv."; exit 1; }

# Crear y activar entorno virtual
if [ ! -d "venv" ]; then
    python3 -m venv venv || { echo "Error creando entorno virtual."; exit 1; }
fi
source venv/bin/activate

# Instalar dependencias de Python
pip install pydub evdev || { echo "Error instalando pydub o evdev."; exit 1; }

# Verificar audio del sistema
if aplay /usr/share/sounds/alsa/Front_Center.wav; then
    echo "Audio verificado: Escuchaste 'Front Center'."
else
    echo "No se detectó audio. Instala y revisa 'pavucontrol' (sudo apt install pavucontrol)."
    exit 1
fi

# Verificar archivos de sonido
if [ ! -f "sounds/gunshot.wav" ] || [ ! -f "sounds/reload.wav" ]; then
    echo "Error: Los archivos sounds/gunshot.wav y/o sounds/reload.wav no existen."
    exit 1
fi

# Ejecutar el programa
echo "Ejecutando disparos-teclado... Presiona Ctrl+C para detener."
python3 main.py -v 1.0
