import pygame

def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
    for img in lista_original:
        lista_girada.append(pygame.transform.flip(img, flip_x, flip_y))
        
    return lista_girada

def reescalar_imagenes(diccionario_animaciones, ancho, alto):

    for clave in diccionario_animaciones:
    
        for i in range(len(diccionario_animaciones[clave])):
    
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))



############################# PLATAFORMA #########################################


class Plataforma:
    def __init__(self, x, y, ancho, alto, imagen, premio, plataforma_visible):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.premio = premio
        self.plataforma_visible = plataforma_visible
    
        if self.plataforma_visible:
            self.imagen = pygame.transform.scale(imagen, (ancho,alto))
        else:
            self.imagen = pygame.Surface((ancho, alto))


        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.velocidad_y = 5
        self.direccion = "arriba"

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def mover(self):
        if self.direccion == "arriba":
            self.y -= self.velocidad_y

            if self.y <= 300:
                self.direccion = "abajo"

        elif self.direccion == "abajo":
            self.y += self.velocidad_y

            if self.y >= 560:
                self.direccion = "arriba"

        self.rectangulo.y = self.y
        



#################################### MICKEY #######################################


personaje_mickey_quieto = [pygame.image.load(r"img\mickey\quieto.png")]

personaje_mickey_corre = [pygame.image.load(r"img\mickey\corre (1).png"),
                          pygame.image.load(r"img\mickey\corre (2).png"),
                          pygame.image.load(r"img\mickey\corre (3).png"),
                          pygame.image.load(r"img\mickey\corre (4).png")]

personaje_mickey_corre_izquierda = girar_imagenes(personaje_mickey_corre, True, False)

personaje_mickey_agacha = [pygame.image.load(r"img\mickey\agacha (1).png"),
                           pygame.image.load(r"img\mickey\agacha (2).png"),
                           pygame.image.load(r"img\mickey\agacha (3).png"),
                           pygame.image.load(r"img\mickey\agacha (4).png"),
                           pygame.image.load(r"img\mickey\agacha (5).png"),
                           pygame.image.load(r"img\mickey\agacha (6).png"),
                           pygame.image.load(r"img\mickey\agacha (7).png"),
                           pygame.image.load(r"img\mickey\agacha (8).png"),
                           pygame.image.load(r"img\mickey\agacha (9).png")]

personaje_mickey_poder = [pygame.image.load(r"img\mickey\poder (1).png"),
                          pygame.image.load(r"img\mickey\poder (2).png"),
                          pygame.image.load(r"img\mickey\poder (3).png"),
                          pygame.image.load(r"img\mickey\poder (4).png"),
                          pygame.image.load(r"img\mickey\poder (5).png"),
                          pygame.image.load(r"img\mickey\poder (6).png"),
                          pygame.image.load(r"img\mickey\poder (7).png"),
                          pygame.image.load(r"img\mickey\poder (8).png"),
                          pygame.image.load(r"img\mickey\poder (9).png")]

personaje_mickey_salta = [pygame.image.load(r"img\mickey\salta (3).png")]


#################################### JACK #######################################

personaje_jack_quieto = [pygame.image.load(r"img\jack\0.png")]

personaje_jack_corre = [pygame.image.load(r"img\jack\10.png"),
                        pygame.image.load(r"img\jack\11.png"),
                        pygame.image.load(r"img\jack\12.png"),
                        pygame.image.load(r"img\jack\13.png"),
                        pygame.image.load(r"img\jack\14.png"),
                        pygame.image.load(r"img\jack\15.png"),
                        pygame.image.load(r"img\jack\16.png"),
                        pygame.image.load(r"img\jack\17.png"),
                        pygame.image.load(r"img\jack\18.png"),
                        pygame.image.load(r"img\jack\19.png")]

personaje_jack_corre_izquierda = girar_imagenes(personaje_jack_corre, True, False)

personaje_jack_salta = [pygame.image.load(r"img\jack\22.png")]

personaje_jack_dispara = [pygame.image.load(r"img\jack\disparo (1).png"),
                          pygame.image.load(r"img\jack\disparo (4).png"),
                          pygame.image.load(r"img\jack\disparo (5).png")]

personaje_jack_dispara_izquierda = girar_imagenes(personaje_jack_dispara, True, False)



#################################### ENEMIGO #######################################

enemigo_camina = [pygame.image.load(r"img\aladin\1.png"),
                  pygame.image.load(r"img\aladin\2.png"),
                  pygame.image.load(r"img\aladin\3.png")]

enemigo_camina_izquierda = girar_imagenes(enemigo_camina, True, False)

enemigo_herida = [pygame.image.load(r"img\aladin\coalicion (1).png"),
                  pygame.image.load(r"img\aladin\coalicion (2).png"),
                  pygame.image.load(r"img\aladin\coalicion (3).png"),
                  pygame.image.load(r"img\aladin\coalicion (4).png"),
                  pygame.image.load(r"img\aladin\coalicion (5).png")]