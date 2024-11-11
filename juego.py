import pygame
import random
from personaje import Player
from enemigo import Enemigo
from bala import crear_bala, Bala  # Importa la función crear_bala
from item import Item

def iniciar_juego(VENTANA, FUENTE, ANCHO, ALTO):
    FPS = 60
    reloj = pygame.time.Clock()
    tiempo_pasado = 0
    tiempo_entre_enemigos = 500
    player = Player(ANCHO / 2, ALTO - 50)
    enemigos = []
    items = []
    balas = []
    puntos = 0
    bonus = 5
    jugando = True
    game_over = False

    def gestionar_teclas(teclas):
        if teclas[pygame.K_a]:
            if player.x >= 0:
                player.x -= player.velocidad
        if teclas[pygame.K_d]:
            if player.x + player.ancho <= ANCHO:
                player.x += player.velocidad

    while jugando:
        if player.vida <= 0:
            game_over = True
            break  # Sale del bucle principal del juego

        tiempo_pasado += reloj.tick(FPS)
        Item.tiempo_pasado += reloj.tick(1000)

        if tiempo_pasado > tiempo_entre_enemigos:
            enemigos.append(Enemigo(random.randint(0, ANCHO), -20))
            tiempo_pasado = 0

        if puntos >= bonus:
            items.append(Item(random.randint(0, ANCHO), -20))
            bonus = puntos+5

        eventos = pygame.event.get()
        teclas = pygame.key.get_pressed()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    crear_bala(player, balas)  # Llama a la función crear_bala

        texto_vida = FUENTE.render(f"Vida: {player.vida}", True, "white")
        texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")
        municion = FUENTE.render(f"Municion: {player.municion}", True, "white")
        texto_bonus = FUENTE.render(f"Bonus: {bonus}", True, "white")

        gestionar_teclas(teclas)

        VENTANA.fill("black")
        player.dibujar(VENTANA)

        # Dibujar items
        for item in items:
            if item.x >= 0 and item.x + item.ancho <= ANCHO:
                item.dibujar(VENTANA)
                item.movimiento()

            if pygame.Rect.colliderect(item.rect, player.rect):
                player.tipo_disparo = item.tipo
                if item.tipo == 3:
                    player.municion = 500
                else:
                 player.municion = 50
                items.remove(item)

            if item.y > ALTO:
                items.remove(item)

        # Dibujar enemigos
        for enemigo in enemigos:
            if enemigo.x >= 0 and enemigo.x + enemigo.ancho <= ANCHO:
                enemigo.dibujar(VENTANA)
                enemigo.movimiento()

            if pygame.Rect.colliderect(player.rect, enemigo.rect):
                player.vida -= 1
                enemigos.remove(enemigo)

            if enemigo.y > ALTO:
                enemigos.remove(enemigo)

            for bala in balas:
                if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                    enemigo.vida -= 1
                    balas.remove(bala)

            if enemigo.vida <= 0:
                enemigos.remove(enemigo)
                puntos += 1

        for bala in balas:
            bala.dibujar(VENTANA)
            bala.movimiento()
            if bala.y < 0:
                balas.remove(bala)

        VENTANA.blit(texto_vida, (10, 10))
        VENTANA.blit(texto_puntos, (100, 10))
        VENTANA.blit(municion, (200, 10))
        VENTANA.blit(texto_bonus, (300, 10))

        pygame.display.update()

    return puntos
