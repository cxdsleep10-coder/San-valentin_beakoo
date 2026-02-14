import asyncio
import pygame

# --- CARGA ULTRA SEGURA ---
def cargar_recurso(nombre_base, size):
    # Prueba todas las extensiones posibles por si acaso
    for ext in [".jpg", ".png", ".jpeg", ".JPG", ".PNG"]:
        try:
            img = pygame.image.load(f"{nombre_base}{ext}").convert_alpha()
            return pygame.transform.scale(img, size)
        except:
            continue
    # Si nada funciona, crea un cuadro rosa de emergencia
    surf = pygame.Surface(size)
    surf.fill((255, 105, 180)) 
    return surf

# ... (dentro de tu función principal)
imgs_fijas = {
    "fondo": cargar_recurso("girasoles", (900, 500)),
    "corazon_portada": cargar_recurso("corazon", (350, 350)),
    "meowl": cargar_recurso("meowl2", (300, 300)),
    "fatality_img": cargar_recurso("fatality", (300, 300)),
}
# Desactiva sonidos para evitar que el navegador bloquee el juego en el móvil
sonido_clic = sonido_sorpresa = None
