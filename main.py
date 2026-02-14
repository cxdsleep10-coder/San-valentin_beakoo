# --- CARGA DE RECURSOS SEGURA ---
    imgs_fijas = {}
    
    # Intentar cargar solo lo vital, si no está, que no rompa el juego
    imgs_fijas["fondo"] = cargar_img("girasoles", (900, 500), False)
    imgs_fijas["corazon_portada"] = cargar_img("corazon", (350, 350))
    imgs_fijas["meowl"] = cargar_img("meowl2", (300, 300), False)
    imgs_fijas["fatality_img"] = cargar_img("fatality", (300, 300), False)
    imgs_fijas["cursor"] = None # Ponemos None para que no busque el archivo cursor.png

    # --- SONIDOS SEGUROS ---
    sonido_clic = sonido_sorpresa = None # Desactiva sonidos por hoy para evitar errores de carga
