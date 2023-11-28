import pygame, sys
from pygame.locals import *
from Class_Personaje import *
from Class_Enemigo import *
from configuraciones import *
from modo import *

##############################INICIALIZACIONES##########################################

#############Pantalla##########
#ANCHO W - ALTO H
W,H = 1200, 700
FPS = 18 #para desacelerar la pantalla

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H)) # en pixeles


#Fondo
fondo = pygame.image.load(r"img\fondos\fondo_aladin.jpg").convert()#Acelera el juego y hace que consuma menos recursos
fondo = pygame.transform.scale(fondo, (W,H))

piso_img = pygame.image.load(r"img\plataformas\plataforma.png")

plataforma_1_img = pygame.image.load(r"img\plataformas\plataforma (2).png")
plataforma_2_img = pygame.image.load(r"img\plataformas\plataforma (4).png")


#PERSONAJES

diccionario_jack = {}

diccionario_jack["Quieto"] = personaje_jack_quieto
diccionario_jack["Derecha"] = personaje_jack_corre
diccionario_jack["Izquierda"] = personaje_jack_corre_izquierda
diccionario_jack["Salta"] = personaje_jack_salta
diccionario_jack["Dispara"] = personaje_jack_dispara
diccionario_jack["Dispara_Izquierda"] = personaje_jack_dispara_izquierda


diccionario_mickey = {}

diccionario_mickey["Quieto"] = personaje_mickey_quieto
diccionario_mickey["Derecha"] = personaje_mickey_corre
diccionario_mickey["Izquierda"] = personaje_mickey_corre_izquierda
diccionario_mickey["Salta"] = personaje_mickey_salta

mickey = Personaje(diccionario_mickey, (50,80), 50, 600, 15)

jack = Personaje(diccionario_jack, (60,120), 50, 600, 10)

personaje_actual = mickey

piso = Plataforma(0, 660, 1200, 50, piso_img, False, True)
plataforma_1 = Plataforma(250, 400, 200, 100, plataforma_1_img, False, True)
plataforma_2 = Plataforma(600, 300, 400, 100, plataforma_2_img, False, True)
plataforma_3 = Plataforma(1100, 100, 100, 50, plataforma_2_img, False, True)



plataformas = [piso, plataforma_1, plataforma_2, plataforma_3]

piso.rectangulo.top = personaje_actual.rectangulo_principal.bottom

lista_enemigos = Enemigo.crear_lista(piso)

flag_disparo = False
tiempo_ultimo_disparo = 0

while True:
    RELOJ.tick(FPS) 
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    keys = pygame.key.get_pressed()

    PANTALLA.blit(fondo,(0,0))
    piso.dibujar(PANTALLA)
    plataforma_1.dibujar(PANTALLA)
    plataforma_1.mover()
    plataforma_2.dibujar(PANTALLA)
    plataforma_3.dibujar(PANTALLA)


    # Guarda la posición del personaje actual
    posicion_actual_x = personaje_actual.rectangulo_principal.x
    posicion_actual_y = personaje_actual.rectangulo_principal.y


    if(keys[pygame.K_TAB]):
        personaje_actual = mickey
        personaje_actual.rectangulo_principal.x = posicion_actual_x
        personaje_actual.rectangulo_principal.y = posicion_actual_y

    elif(keys[pygame.K_SPACE]):
        personaje_actual = jack
        personaje_actual.rectangulo_principal.x = posicion_actual_x
        personaje_actual.rectangulo_principal.y = posicion_actual_y



    for enemigo in lista_enemigos:
        enemigo.actualizar(PANTALLA)

    if(keys[pygame.K_RIGHT]):
        personaje_actual.que_hace = "Derecha"
        personaje_actual.direccion = "Derecha"
    elif(keys[pygame.K_LEFT]):
        personaje_actual.que_hace = "Izquierda"
        personaje_actual.direccion = "Izquierda"
    elif(keys[pygame.K_UP]):
        personaje_actual.que_hace = "Salta"
    else: 
        personaje_actual.que_hace = "Quieto"


    if(keys[pygame.K_LSHIFT]) and personaje_actual == jack:
        
        tiempo_actual = pygame.time.get_ticks()
        
        if tiempo_actual - tiempo_ultimo_disparo >= 1000:
            tiempo_ultimo_disparo = tiempo_actual
            personaje_actual.que_hace = "Dispara"
            flag_disparo = True
            personaje_actual.disparar(PANTALLA, lista_enemigos, plataformas)


    personaje_actual.actualizar(PANTALLA, plataformas, personaje_actual.direccion, lista_enemigos)


    if get_mode() == True:
        pygame.draw.rect(PANTALLA,"green",personaje_actual.rectangulo_principal, 3)

        for plataforma in plataformas:
            pygame.draw.rect(PANTALLA,"red",piso.rectangulo,3)
            pygame.draw.rect(PANTALLA,"black",plataforma_1.rectangulo,3)
            pygame.draw.rect(PANTALLA,"black",plataforma_2.rectangulo,3)

        for enemigo in lista_enemigos:
            pygame.draw.rect(PANTALLA,"white",enemigo.rectangulo,3)

    pygame.display.update()