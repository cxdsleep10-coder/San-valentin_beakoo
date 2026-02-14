# --- CARGA SIMPLIFICADA (PARA QUE NO DE PANTALLA NEGRA) ---
    def cargar_fácil(nombre_archivo, size):
        try:
            img = pygame.image.load(nombre_archivo).convert_alpha()
            return pygame.transform.scale(img, size)
        except:
            # Si la imagen no carga, crea un cuadro de color para que el juego siga
            surf = pygame.Surface(size)
            surf.fill((200, 0, 100)) 
            return surf

    # USA LOS NOMBRES EXACTOS QUE TIENES EN GITHUB
    imgs_fijas = {
        "fondo": cargar_fácil("girasoles.jpg", (900, 500)),
        "corazon_portada": cargar_fácil("corazon.png", (350, 350)),
        "meowl": cargar_fácil("meowl2.jpeg", (300, 300)),
        "fatality_img": cargar_fácil("fatality.png", (300, 300)),
        "cursor": None # Quitamos el cursor para evitar fallos
    }

    sonido_clic = sonido_sorpresa = None
