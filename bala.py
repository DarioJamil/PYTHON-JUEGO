import pygame

pygame.mixer.init()
SONIDO_DISPARO = pygame.mixer.Sound('recursos/disparo.mp3')

class Bala:
    def __init__(self, x, y, velocidadx=0):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.velocidad = 5  # Velocidad en el eje Y
        self.velocidadx = velocidadx  # Velocidad en el eje X (diagonal)
        self.color = "white"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load('recursos/bala(1).png')
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.imagen = pygame.transform.rotate(self.imagen, 180)
       

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        ventana.blit(self.imagen, (self.x, self.y))

    def movimiento(self):
        self.y -= self.velocidad
        self.x += self.velocidadx  # Movimiento en diagonal

    
def crear_bala(player, balas):
    if player.tipo_disparo == 0:
        balas.append(Bala(player.rect.x + 11, player.rect.y - 4))
    elif player.tipo_disparo == 1:
        balas.append(Bala(player.rect.x, player.rect.y - 4))
        balas.append(Bala(player.rect.x + 22, player.rect.y - 4))
        player.municion -= 2
        if player.municion <= 0:
            player.tipo_disparo = 0
            player.municion = 0
    elif player.tipo_disparo == 2:
        balas.append(Bala(player.rect.x, player.rect.y - 4))
        balas.append(Bala(player.rect.x + 11, player.rect.y - 4))
        balas.append(Bala(player.rect.x + 22, player.rect.y - 4))
        player.municion -= 3
        if player.municion <= 0:
            player.tipo_disparo = 0
            player.municion = 0
    elif player.tipo_disparo == 3:
        balas.append(Bala(player.rect.x -11, player.rect.y - 4, velocidadx=-2))
        balas.append(Bala(player.rect.x, player.rect.y - 4))
        balas.append(Bala(player.rect.x + 11, player.rect.y - 4))
        balas.append(Bala(player.rect.x + 22, player.rect.y - 4))
        balas.append(Bala(player.rect.x + 33, player.rect.y - 4, velocidadx=+2))
        player.municion -= 5
        if player.municion <= 0:
            player.tipo_disparo = 0
            player.municion = 0
    SONIDO_DISPARO.play()
