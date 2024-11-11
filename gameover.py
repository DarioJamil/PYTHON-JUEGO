import pygame
import sys

ANCHO = 500
ALTO = 500

def mostrar_gameover(puntos):
    pygame.init()
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    FUENTE = pygame.font.SysFont("Comic Sans", 40)
    reloj = pygame.time.Clock()

    nombre = ""
    input_active = True
    game_over = True

    while game_over:
        VENTANA.fill("black")
        game_over_texto = FUENTE.render("GAME OVER", True, "white")
        reiniciar_texto = FUENTE.render("1. Volver a Jugar", True, "white")
        salir_texto = FUENTE.render("2. Salir", True, "white")
        nombre_texto = FUENTE.render(f"Nombre: {nombre}", True, "white")

        VENTANA.blit(game_over_texto, (ANCHO // 2 - 100, ALTO // 2 - 100))
        VENTANA.blit(reiniciar_texto, (ANCHO // 2 - 150, ALTO // 2 - 20))
        VENTANA.blit(salir_texto, (ANCHO // 2 - 150, ALTO // 2 + 40))
        VENTANA.blit(nombre_texto, (ANCHO // 2 - 150, ALTO // 2 + 100))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    if nombre == "":
                        nombre = "---"
                    with open('recursos/puntuaciones.txt', 'a') as archivo:
                        archivo.write(f"{nombre} - {puntos}\n")
                    # pygame.quit()
                    return "jugar"  # Retorna a la opción para volver a jugar

                if evento.key == pygame.K_2:
                    if nombre == "":
                        nombre = "---"
                    with open('recursos/puntuaciones.txt', 'a') as archivo:
                        archivo.write(f"{nombre} - {puntos}\n")
                    pygame.quit()
                    sys.exit()  # Salir del juego

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif evento.key == pygame.K_RETURN:
                    if nombre == "":
                        nombre = "---"
                    with open('recursos/puntuaciones.txt', 'a') as archivo:
                        archivo.write(f"{nombre} - {puntos}\n")
                    pygame.quit()
                    return "jugar"
                else:
                    nombre += evento.unicode
