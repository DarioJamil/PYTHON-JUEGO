# menu.py
import pygame

ANCHO = 500
ALTO = 500

def mostrar_menu():
    pygame.init()
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    FUENTE = pygame.font.SysFont("Comic Sans", 40)
    jugando = True
    opcion_seleccionada = None

    while jugando:
        VENTANA.fill("black")
        
        # Textos del menú
        titulo_texto = FUENTE.render("MENU PRINCIPAL", True, "white")
        jugar_texto = FUENTE.render("1. Jugar", True, "white")
        salir_texto = FUENTE.render("2. Salir", True, "white")
        
        VENTANA.blit(titulo_texto, (ANCHO // 2 - 150, ALTO // 2 - 100))
        VENTANA.blit(jugar_texto, (ANCHO // 2 - 100, ALTO // 2 - 20))
        VENTANA.blit(salir_texto, (ANCHO // 2 - 100, ALTO // 2 + 40))
        
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
                opcion_seleccionada = "salir"
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    opcion_seleccionada = "jugar"
                    jugando = False  # Sale del menú y comienza el juego
                if evento.key == pygame.K_2:
                    opcion_seleccionada = "salir"
                    jugando = False  # Sale del menú y cierra el programa

    # pygame.quit()  # Finaliza Pygame cuando se sale del menú
    return opcion_seleccionada
