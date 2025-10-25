#!/bin/bash

# Script para ejecutar disparos-teclado (para usuarios con entorno ya configurado)
echo "Iniciando disparos-teclado..."

# Verificar que estamos en el directorio correcto
if [ ! -f "main.py" ] || [ ! -d "sounds" ]; then
    echo "Error: Asegúrate de estar en el directorio ~/disparos-teclado y que main.py y la carpeta sounds/ existan."
    exit 1
fi

# Verificar archivos de sonido
if [ ! -f "sounds/gunshot.wav" ] || [ ! -f "sounds/reload.wav" ]; then
    echo "Error: Los archivos sounds/gunshot.wav y/o sounds/reload.wav no existen."
    exit 1
fi

# Verificar entorno virtual
if [ ! -d "venv" ]; then
    echo "Error: El entorno virtual (venv) no existe. Ejecuta run-disparos-teclado.sh primero."
    exit 1
fi

# Activar entorno virtual
source venv/bin/activate

# Ejecutar el programa
echo "Ejecutando disparos-teclado... Presiona Ctrl+C para detener."
python3 main.py -v 1.0
