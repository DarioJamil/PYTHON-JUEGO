import pygame

class Enemigo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 30 
        self.alto = 30 
        self.velocidad = 3
        self.color ="red"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load('recursos/enemigo.png')
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.vida = 1

    def dibujar(self, ventana):
             # esta linea cambia las coodenadas 
             self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
             #pygame.draw.rect(ventana, self.color, self.rect)
             ventana.blit(self.imagen, (self.x, self.y)) 
    
    def movimiento(self):
          self.y += self.velocidad

        