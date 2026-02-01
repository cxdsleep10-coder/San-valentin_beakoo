import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    font = pygame.font.SysFont("arial", 50)
    
    while True:
        screen.fill((255, 0, 0)) # Esto pondrá la pantalla ROJA
        txt = font.render("SI VES ESTO ROJO, FUNCIONA", True, (255, 255, 255))
        screen.blit(txt, (100, 200))
        
        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())
