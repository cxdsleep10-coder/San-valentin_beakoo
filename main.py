import pygame
import sys
import random
import asyncio  # IMPORTANTE PARA WEB

async def main():
    # Inicialización
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Para mi querida Beako 🌻")

    # --- FUENTES ---
    try:
        font = pygame.font.SysFont("arial", 24, bold=True)
        titulo_font = pygame.font.SysFont("arial", 50, bold=True)
        p_font = pygame.font.SysFont("segoe ui emoji", 24)
    except:
        font = titulo_font = p_font = pygame.font.Font(None, 32)

    # --- SISTEMA DE PARTÍCULAS ---
    particulas = []
    for _ in range(35):
        particulas.append([random.randint(0, WIDTH), random.randint(-500, 0), random.uniform(1.5, 3.5), random.choice(["❤️", "🌸", "🌻", "✨"])])

    # --- FUNCIÓN DE CARGA ---
    def cargar_img(nombre, size=(280, 280), transparente=True):
        if not nombre: return None
        for ext in [".png", ".jpg", ".jpeg"]:
            try:
                img = pygame.image.load(f"{nombre}{ext}").convert_alpha()
                if transparente:
                    img.set_colorkey((255, 255, 255)) 
                return pygame.transform.scale(img, size)
            except: continue
        return None

    # Carga de recursos (Nota: Cambié meowl (2) por meowl2)
    imgs_fijas = {
        "fondo": cargar_img("girasoles", (900, 500), False),
        "corazon_portada": cargar_img("corazon", (350, 350)),
        "meowl": cargar_img("meowl2", (300, 300), False),
        "fatality_img": cargar_img("fatality", (300, 300), False),
        "cursor": cargar_img("cursor", (40, 40)) 
    }

    # --- SONIDOS ---
    try:
        sonido_clic = pygame.mixer.Sound("clic.wav")
        sonido_sorpresa = pygame.mixer.Sound("fatality.mp3") 
    except:
        sonido_clic = sonido_sorpresa = None

    try:
        pygame.mixer.music.load("cancion.mp3")
        pygame.mixer.music.play(-1)
    except: pass

    # --- GUION ---
    guion = [
        ("cedric", "Beako, aunque estemos lejos, las ganas de sonreír no tienen Wi-Fi. 🌅", "cedric1", False),
        ("beako", "¿De verdad lo sientes así aunque la distancia sea mucha?", "beako1", False),
        ("cedric", "¡Claro! Eres más dulce que cualquier dulce... 🍬", "cedric2", False),
        ("cedric", "Pero cuidado con el sol, te puedes derretir, bombón. ☀️", "cedric2", False),
        ("cedric", "¿Tu papá es panadero? Porque eres un bizcocho y el más dulce. 🥐", "cedric1", False),
        ("beako", "¡Qué malo es ese chiste! Pero admito que me hizo reír.", "beako3", False),
        ("cedric", "Max y Chloe saben que lo real no se rompe con la distancia. 🦋", "cedric1", False),
        ("beako", "Enserio, wow eso es lindo cece", "beako2", False),
        ("cedric", "Exacto. No eres solo una princesa, eres una reina. 👑", "cedric2", False),
        ("cedric", "¿Puedo ser tu caballero? No porque seas indefensa,", "cedric1", False),
        ("cedric", "sino porque tú lo permites. ⚔️", "cedric2", False),
        ("cedric", "Entonces... ¿Quieres ser mi San Valentín?", "cedric2", True)
    ]

    final_si = [("cedric", "¡Espera, ¿real?! ¡Wowser, gracias! ❤️", "cedric2"), ("cedric", "Espero que te haya sacado una sonrisa, Beako.", "cedric1")]
    final_no = [("cedric", "Entiendo... bueno, ¡al menos el código no falló! jaja", "cedric3"), ("cedric", "Gracias por jugar de todas formas.", "cedric1")]

    # Estados
    estado = "INICIO"; indice = 0; indice_final = 0
    esperando_respuesta = False; resultado_final = ""
    pygame.mouse.set_visible(False)

    # --- BUCLE PRINCIPAL ---
    while True:
        mouse_pos = pygame.mouse.get_pos()
        btn_start = pygame.Rect(WIDTH//2 - 75, 380, 150, 50)
        btn_si = pygame.Rect(300, 250, 120, 50)
        btn_no = pygame.Rect(480, 250, 120, 50)
        btn_reinicio = pygame.Rect(WIDTH//2 - 100, 420, 200, 45)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if estado == "INICIO" and btn_start.collidepoint(mouse_pos):
                    if sonido_clic: sonido_clic.play()
                    estado = "JUEGO"
                
                elif estado == "JUEGO":
                    if esperando_respuesta:
                        if btn_si.collidepoint(mouse_pos):
                            if sonido_clic: sonido_clic.play()
                            estado = "DIALOGO_FINAL"; resultado_final = "SI"
                        elif btn_no.collidepoint(mouse_pos):
                            pygame.mixer.music.pause()
                            if sonido_sorpresa: sonido_sorpresa.play()
                            estado = "DIALOGO_FINAL"; resultado_final = "NO"
                    else:
                        if sonido_clic: sonido_clic.play()
                        if indice < len(guion) - 1:
                            indice += 1
                            if guion[indice][3]: esperando_respuesta = True
                
                elif estado == "DIALOGO_FINAL":
                    lista = final_si if resultado_final == "SI" else final_no
                    if indice_final < len(lista) - 1: indice_final += 1
                    else: estado = "PANTALLA_CIERRE"

                elif estado == "PANTALLA_CIERRE":
                    if btn_reinicio.collidepoint(mouse_pos):
                        pygame.mixer.music.unpause()
                        if not pygame.mixer.music.get_busy(): pygame.mixer.music.play(-1)
                        estado = "INICIO"; indice = 0; indice_final = 0
                        esperando_respuesta = False; resultado_final = ""

        # DIBUJO
        screen.fill((15, 10, 25))
        for p in particulas:
            p[1] += p[2]
            if p[1] > HEIGHT: p[1] = -20; p[0] = random.randint(0, WIDTH)
            screen.blit(p_font.render(p[3], True, (255,255,255)), (p[0], p[1]))

        if estado == "INICIO":
            if imgs_fijas["corazon_portada"]: screen.blit(imgs_fijas["corazon_portada"], (WIDTH//2 - 175, 40))
            pygame.draw.rect(screen, (200, 40, 80), btn_start, border_radius=20)
            screen.blit(font.render("START", True, (255, 255, 255)), (WIDTH//2 - 38, 392))

        elif estado in ["JUEGO", "DIALOGO_FINAL"]:
            if imgs_fijas["fondo"]: screen.blit(imgs_fijas["fondo"], (0, 0))
            lista = guion if estado == "JUEGO" else (final_si if resultado_final == "SI" else final_no)
            idx = indice if estado == "JUEGO" else indice_final
            pj, txt, img_n = lista[idx][:3]
            img_actual = cargar_img(img_n)
            if img_actual: screen.blit(img_actual, (120 if pj == "cedric" else 500, 70))
            pygame.draw.rect(screen, (0, 0, 0, 230), (50, 350, 800, 120), border_radius=15)
            color_nom = (255, 215, 0) if pj == "cedric" else (255, 105, 180)
            screen.blit(font.render(pj.upper(), True, color_nom), (75, 365))
            screen.blit(font.render(txt, True, (255, 255, 255)), (75, 410))
            if esperando_respuesta and estado == "JUEGO":
                pygame.draw.rect(screen, (50, 200, 50), btn_si, border_radius=12)
                pygame.draw.rect(screen, (200, 50, 50), btn_no, border_radius=12)
                screen.blit(font.render("SÍ", True, (255,255,255)), (345, 260))
                screen.blit(font.render("NO", True, (255,255,255)), (520, 260))

        elif estado == "PANTALLA_CIERRE":
            screen.blit(titulo_font.render("FINAL", True, (255, 215, 0)), (WIDTH//2 - 70, 30))
            img_final = imgs_fijas["meowl"] if resultado_final == "SI" else imgs_fijas["fatality_img"]
            if img_final: screen.blit(img_final, (WIDTH//2 - 150, 100))
            pygame.draw.rect(screen, (60, 60, 180), btn_reinicio, border_radius=15)
            screen.blit(font.render("REINICIAR", True, (255, 255, 255)), (WIDTH//2 - 55, 430))

        if imgs_fijas["cursor"]: screen.blit(imgs_fijas["cursor"], mouse_pos)

        pygame.display.flip()
        await asyncio.sleep(0) # ESTA LÍNEA ES MAGIA PARA EL MÓVIL

asyncio.run(main())
