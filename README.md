# Rick & Morty - API Explorer (Secure Edition)

Aplicación de escritorio desarrollada en Python para la gestión y visualización de personajes del multiverso de Rick & Morty. El proyecto cumple con los estándares de programación asíncrona, seguridad y gestión de memoria exigidos en la rúbrica.

## 🛠️ Cumplimiento de la Rúbrica

* Diversidad de Endpoints (1.00 pts): Consumo de rutas de listado (/character) y detalle de entidad.
* Mapeo de Entidades (1.25 pts): Uso de la clase Personaje con método @classmethod desde_json.
* Separación de Hilos (1.50 pts): Uso de threading para evitar el bloqueo de la interfaz (UI).
* Caché y Memoria (1.50 pts): Sistema de caché en memoria (cache_fotos) y uso de BytesIO.
* Documentación (0.75 pts): Comentarios tipo Javadoc en el código.
* Dockerización (1.00 pts EXTRA): Archivo Dockerfile funcional incluido en el repositorio.

## 🚀 Instalación

1. Instalar dependencias:
pip install customtkinter requests pillow

## 📦 Ejecución

python main.py

## 🐳 Docker

Para construir la imagen:
docker build -t rick-morty-app .
