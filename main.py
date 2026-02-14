# --- CARGA ULTRA SEGURA ---
    def cargar_fácil(nombre_archivo, size):
        try:
            # Intenta cargar el archivo que ya renombraste en GitHub
            img = pygame.image.load(nombre_archivo).convert_alpha()
            return pygame.transform.scale(img, size)
        except Exception as e:
            print(f"Error cargando {nombre_archivo}: {e}")
            # Si falla, crea un cuadro rosa para que el juego NO se quede en negro
            surf = pygame.Surface(size)
            surf.fill((255, 105, 180)) 
            return surf

    # Nombres que ya corregiste en tu GitHub:
    imgs_fijas = {
        "fondo": cargar_fácil("girasoles.jpg", (900, 500)),
        "corazon_portada": cargar_fácil("corazon.png", (350, 350)),
        "meowl": cargar_fácil("meowl2.jpg", (300, 300)),
        "fatality_img": cargar_fácil("fatality.jpg", (300, 300)),
        "cursor": None # Mejor sin cursor para evitar líos hoy
    }

    # Desactivamos sonidos momentáneamente para asegurar que cargue en el móvil
    sonido_clic = sonido_sorpresa = None
