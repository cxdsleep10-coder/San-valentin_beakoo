import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    font = pygame.font.SysFont("Arial", 40)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        screen.fill((255, 182, 193)) # Fondo Rosa
        texto = font.render("¡Ya funciona! Cargando regalo...", True, (255, 255, 255))
        screen.blit(texto, (200, 200))
        
        pygame.display.flip()
        await asyncio.sleep(0) # Esto es lo que evita que se quede en blanco

asyncio.run(main())
