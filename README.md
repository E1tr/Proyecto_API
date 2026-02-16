
**Proyecto**: Rick & Morty - Selector de Personajes

Descripción

- **Breve**: Aplicación de escritorio en Python que muestra personajes de la API pública de Rick and Morty. Interfaz construida con `customtkinter`, recuperación de datos mediante `requests` y manejo de imágenes con `Pillow`.

Características

- **Interfaz GUI**: Panel lateral con lista de personajes y panel de detalle.
- **Carga asíncrona**: Peticiones en hilos para no bloquear la UI.
- **Caché de imágenes**: Evita descargas repetidas durante la sesión.

Requisitos

- **Python**: 3.8 o superior (recomendado 3.10+).
- **Dependencias**: `customtkinter`, `requests`, `Pillow`.

Instalación rápida

1. Crear y activar un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

1. Instalar dependencias:

```powershell
pip install customtkinter requests pillow
```

Uso

- Ejecutar la aplicación:

```powershell
python main.py
```

- Pulsa "Cargar Personajes" para obtener la lista inicial. Haz clic en cualquiera para ver la imagen y los datos.

Estructura del proyecto

- `main.py`: código principal de la aplicación (interfaz, cliente HTTP y entidad `Personaje`).
- `README.mD`: este archivo.

Notas de implementación

- La clase `RickAndMortyClient` consume `https://rickandmortyapi.com/api` y devuelve objetos `Personaje` usando el método `desde_json`.
- Las operaciones de red y carga de imágenes se realizan en hilos para mantener la UI responsiva.

Próximos pasos sugeridos

- Añadir `requirements.txt` para fijar versiones.
- Añadir manejo de paginación de la API para cargar más personajes.
- Añadir pruebas unitarias para el cliente HTTP y la transformación a `Personaje`.

Contribuciones

- Si quieres contribuir, abre un issue o un pull request con cambios pequeños y descriptivos.

Licencia

- Añade aquí la licencia que prefieras (por ejemplo, MIT). Actualmente no se incluye un archivo de licencia en el repositorio.

Contacto

- Si necesitas ayuda o quieres que prepare `requirements.txt` y un script de ejecución, dímelo y lo agrego.
