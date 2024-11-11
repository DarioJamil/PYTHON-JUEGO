import pygame
import random

class Item:
    tiempo_pasado = 0
    tiempo_entre_item = 500

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 30 
        self.alto = 30 
        self.velocidady = 1
        self.velocidadx = 0
        self.tipo = random.randint(1, 3)
        if self.tipo == 1:
            self.color = "red"
            self.imagen = pygame.image.load('recursos/X2.png')
        elif self.tipo == 2:
            self.color = "green"
            self.imagen = pygame.image.load('recursos/X3.png')
        elif self.tipo == 3:
            self.color = "blue"
            self.imagen = pygame.image.load('recursos/X5.png')
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        #self.imagen = pygame.image.load('recursos/enemigo.png')
        #self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
       

    def dibujar(self, ventana):
             # esta linea cambia las coodenadas 
             self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
            #pygame.draw.rect(ventana, self.color, self.rect)
             ventana.blit(self.imagen, (self.x, self.y)) 
    
    def movimiento(self):
          self.y += self.velocidady
         # self.x += self.velocidadx

        