# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Instalamos librerías del sistema necesarias para la interfaz gráfica (Tkinter)
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiamos los archivos
COPY . .

# Instalamos dependencias de Python
RUN pip install customtkinter requests Pillow

# Comando para ejecutar
CMD ["python", "main.py"]