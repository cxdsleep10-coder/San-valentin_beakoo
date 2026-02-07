import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    
    # Cargamos cada cosa por separado para que no se rompa
    beako = None
    cedric = None
    corazon = None
    
    try:
        beako = pygame.image.load("beako1.png")
    except: pass
    
    try:
        cedric = pygame.image.load("cedric1.png")
    except: pass
    
    try:
        corazon = pygame.image.load("corazon.png")
    except: pass

    try:
        pygame.mixer.music.load("cancion.mp3")
        pygame.mixer.music.play(-1)
    except: pass

    fuente = pygame.font.SysFont("Arial", 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        screen.fill((255, 182, 193)) # Fondo Rosa
        
        # Dibujar solo si cargaron
        if beako: screen.blit(beako, (50, 100))
        if cedric: screen.blit(cedric, (600, 100))
        if corazon: screen.blit(corazon, (380, 150))

        msg = fuente.render("¡Para Beako! Mira tus archivos cargados", True, (255, 255, 255))
        screen.blit(msg, (220, 400))
        
        pygame.display.flip()
        await asyncio.sleep(0) 

asyncio.run(main())
