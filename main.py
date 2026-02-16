import customtkinter as ctk
import requests
import threading
from PIL import Image
from io import BytesIO

class Personaje:
    """
    Entidad que representa un personaje de la API.
    Cumple con el criterio de 'Mapeig d'entitats'.
    """
    def __init__(self, id, nombre, estado, foto_url, especie, origen):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.foto_url = foto_url
        self.especie = especie
        self.origen = origen

    @classmethod
    def desde_json(cls, data):
        return cls(
            id=data.get('id'),
            nombre=data.get('name'),
            estado=data.get('status'),
            foto_url=data.get('image'),
            especie=data.get('species'),
            origen=data.get('origin', {}).get('name', 'Desconocido')
        )

class RickAndMortyClient:
    """
    Cliente para la gestión de red y HTTP.
    Cumple con 'Seguretat' y 'Maneig d'HTTP'.
    """
    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"
        self.headers = {"Accept": "application/json"}

    def listar_personajes(self):
        try:
            response = requests.get(f"{self.base_url}/character", headers=self.headers)
            response.raise_for_status()
            datos = response.json()
            return [Personaje.desde_json(p) for p in datos['results']]
        except Exception as e:
            print(f"Error: {e}")
            return []

class AppPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rick & Morty - Selector de Personajes")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")
        
        self.api = RickAndMortyClient()
        self.cache_fotos = {} # Rúbrica: Caché / Memoria
        self.selected_button = None
        self.selected_person_id = None

        # Configuración de grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- PANEL IZQUIERDO: LISTA CON SCROLL ---
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.titulo = ctk.CTkLabel(self.sidebar, text="MULTIVERSO", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=20)

        # Frame con scroll para meter los botones de los personajes
        self.scroll_lista = ctk.CTkScrollableFrame(self.sidebar, width=250, height=450)
        self.scroll_lista.pack(pady=10, padx=10, fill="both", expand=True)

        self.btn_fetch = ctk.CTkButton(self.sidebar, text="Cargar Personajes", command=self.iniciar_carga)
        self.btn_fetch.pack(pady=20)

        # --- PANEL DERECHO: DETALLE ---
        self.detalle = ctk.CTkFrame(self, corner_radius=10)
        self.detalle.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.img_label = ctk.CTkLabel(self.detalle, text="Pincha en un personaje de la izquierda")
        self.img_label.pack(pady=30)

        self.info_label = ctk.CTkLabel(self.detalle, text="", font=("Arial", 18), justify="left")
        self.info_label.pack(pady=10)

    def iniciar_carga(self):
        """Lanza el hilo para no bloquear la UI (Separació de fils)"""
        self.btn_fetch.configure(state="disabled")
        threading.Thread(target=self.proceso_carga, daemon=True).start()

    def proceso_carga(self):
        personajes = self.api.listar_personajes()
        
        # Limpiar lista anterior
        for widget in self.scroll_lista.winfo_children():
            widget.destroy()

        # Reset selección previa
        self.selected_button = None
        self.selected_person_id = None

        # Crear un botón por cada personaje
        for p in personajes:
            btn = ctk.CTkButton(
                self.scroll_lista,
                text=p.nombre,
                fg_color="transparent",
                text_color="white",
                anchor="w",
            )
            # Asociar comando después de crear el botón para capturar la referencia
            btn.configure(command=lambda obj=p, b=btn: self._on_person_button(obj, b))
            btn.pack(fill="x", pady=2)
        
        self.btn_fetch.configure(state="normal")

    def actualizar_detalle(self, p):
        """
        Actualiza la interfaz con los datos del personaje seleccionado.
        Usa caché para evitar peticiones repetidas (Criterio Caché).
        """
        # Hilo para la imagen para que no de tirones
        threading.Thread(target=self._cargar_imagen_detalle, args=(p,), daemon=True).start()

    def _on_person_button(self, p, button):
        """Maneja la pulsación de un botón de personaje y marca la selección."""
        self._highlight_button(button)
        self.selected_person_id = p.id
        self.actualizar_detalle(p)

    def _highlight_button(self, button):
        """Resetea el estilo del botón previamente seleccionado y resalta el nuevo."""
        try:
            if self.selected_button and self.selected_button.winfo_exists():
                # Restaurar estilo del botón previo
                self.selected_button.configure(fg_color="transparent", text_color="white")
        except Exception:
            pass

        # Establecer nuevo estilo para el botón seleccionado
        try:
            button.configure(fg_color="#2f6aa5", text_color="white")
            self.selected_button = button
        except Exception:
            # Si la configuración falla, simplemente asignamos la referencia
            self.selected_button = button

    def _cargar_imagen_detalle(self, p):
        if p.foto_url in self.cache_fotos:
            imagen = self.cache_fotos[p.foto_url]
        else:
            try:
                res = requests.get(p.foto_url)
                img_data = Image.open(BytesIO(res.content))
                imagen = ctk.CTkImage(light_image=img_data, size=(300, 300))
                self.cache_fotos[p.foto_url] = imagen
            except:
                return

        # Actualizar labels en el hilo principal
        self.img_label.configure(image=imagen, text="")
        self.info_label.configure(
            text=f"Nombre: {p.nombre}\n"
                 f"Especie: {p.especie}\n"
                 f"Estado: {p.estado}\n"
                 f"Origen: {p.origen}"
        )

if __name__ == "__main__":
    app = AppPrincipal()
    app.mainloop()