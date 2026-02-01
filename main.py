import pygame
import asyncio
import sys

# Configuración necesaria para la web
async def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    pygame.display.set_caption("Para Beako")
    clock = pygame.time.Clock()

    # Colores
    ROSA = (255, 182, 193)
    BLANCO = (255, 255, 255)
    
    fuente = pygame.font.SysFont("Arial", 30)

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar fondo
        screen.fill(ROSA)
        
        # Texto de prueba (si ves esto, ya no está en blanco)
        mensaje = fuente.render("¡Cargando el regalo de Beako!", True, BLANCO)
        screen.blit(mensaje, (250, 200))

        pygame.display.flip()
        
        # ESTA LÍNEA es la que hace que funcione en internet
        await asyncio.sleep(0)
        clock.tick(60)

# Ejecutar el juego
asyncio.run(main())
