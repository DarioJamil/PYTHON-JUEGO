import pygame

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 40 
        self.alto = 40
        self.velocidad = 5
        self.color ="blue"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load('recursos/player.png')
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
       # self.imagen = pygame.transform.rotate(self.imagen, 90)
        self.vida = 2
        self.tipo_disparo = 0
        self.municion = 0

    def dibujar(self, ventana):
             # esta linea cambia las coodenadas 
             self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
           #  pygame.draw.rect(ventana, self.color, self.rect)
             ventana.blit(self.imagen, (self.x, self.y)) 

        