import pygame
from menu import mostrar_menu
from gameover import mostrar_gameover
from juego import iniciar_juego

pygame.init()
# pygame.mixer.init()

ANCHO = 500
ALTO = 500
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FPS = 60
FUENTE = pygame.font.SysFont("Comic Sans", 10)
# SONIDO_DISPARO = pygame.mixer.Sound('recursos/disparo.mp3')

def main():
    corriendo = True  # Controla el bucle principal del juego

    while corriendo:
        # Mostrar el menú principal
        opcion = mostrar_menu()
        print(f"Menú seleccionado: {opcion}")

        # Si seleccionamos la opción "jugar"
        if opcion == "jugar":
            # Iniciar el juego y obtener la puntuación final
            puntos = iniciar_juego(VENTANA, FUENTE, ANCHO, ALTO)

            # Mostrar la pantalla de Game Over
            opcion_gameover = mostrar_gameover(puntos)

            if opcion_gameover == "salir":
                corriendo = False  # Salir del juego
            # Si seleccionamos "jugar", volvemos al menú
        elif opcion == "salir":
            corriendo = False  # Salir del bucle principal

    # Al salir del bucle, cerrar pygame
    pygame.quit()

if __name__ == "__main__":
    main()
