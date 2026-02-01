import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    
    # Esto usa los archivos que YA TIENES subidos
    try:
        beako = pygame.image.load("beako1.png")
        cedric = pygame.image.load("cedric1.png")
        corazon = pygame.image.load("corazon.png")
        pygame.mixer.music.load("cancion.mp3")
        pygame.mixer.music.play(-1)
    except:
        pass 

    fuente = pygame.font.SysFont("Arial", 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        screen.fill((255, 182, 193)) # Fondo Rosa
        
        # Poner las fotos que ya subiste
        try:
            screen.blit(beako, (50, 100))
            screen.blit(cedric, (600, 100))
            screen.blit(corazon, (380, 150))
        except:
            pass

        msg = fuente.render("¡Para Beako! Mira tus archivos cargados", True, (255, 255, 255))
        screen.blit(msg, (220, 400))
        
        pygame.display.flip()
        await asyncio.sleep(0) 

asyncio.run(main())
