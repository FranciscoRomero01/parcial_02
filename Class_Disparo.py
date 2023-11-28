import pygame
from configuraciones import *

class Disparo:
    def __init__(self, x, y, imagen, velocidad_x, pantalla, direccion):
        self.pantalla = pantalla
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (80, 80))
        self.rectangulo = self.imagen.get_rect()
        print(self.rectangulo)
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion

        self.velocidad_x = velocidad_x

    def dibujar(self):
        self.pantalla.blit(self.imagen, (500 + 60, self.rectangulo.y))

    def mover(self):

        if self.direccion == "Derecha":
            self.rectangulo.x += self.velocidad_x

        else:
            self.rectangulo.x -= self.velocidad_x

        # Actualiza la posición real del rectángulo
        self.pantalla.blit(self.imagen, self.rectangulo)
        pygame.draw.rect(self.pantalla,"blue",self.rectangulo,3)



    def verificar_coalicion_enemigo(self, lista):
        i = 0

        while i < len(lista):

            elemento = lista[i]

            if self.rectangulo.colliderect(elemento.rectangulo):
                print("SS")

            i += 1
                