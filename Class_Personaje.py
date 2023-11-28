from configuraciones import *
from Class_Disparo import *




class Personaje:
    def __init__(self, animaciones, tamaño, pos_x, pos_y, velocidad):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        #crear rect con el tam y la pos 
        self.rectangulo_principal = animaciones["Quieto"][0].get_rect()
        print(self.rectangulo_principal)

        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.que_hace = "Quieto"
        self.direccion = "Derecha"
        self.animacion_actual = self.animaciones["Quieto"]
        
        ####SALTO######
        
        self.desplazamiento_y = 0 
        self.potencia_salto = -25 
        self.limite_velocidad_salto = 25 
        self.esta_saltando = False
        self.gravedad = 2

        #### DISPARO ####
        self.lista_disparos = []

        #### VIDAS ####
        self.vidas = 5

    def caminar(self, pantalla):
        
        velocidad_actual =  self.velocidad
        if self.que_hace == "Izquierda":
            velocidad_actual *= -1
            
        nueva_posicion = self.rectangulo_principal.x + velocidad_actual
        if nueva_posicion > 0 and nueva_posicion <= (pantalla.get_width() - self.rectangulo_principal.width):
            self.rectangulo_principal.x += velocidad_actual


    def animar(self, pantalla, animacion):

        self.animacion_actual = self.animaciones[animacion]

        largo = len(self.animacion_actual)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
            
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)

        self.contador_pasos +=1
    
    
    def actualizar(self, pantalla, plataformas, direccion, lista_enemigos):
            
        match self.que_hace:
            case "Derecha":
                if not self.esta_saltando: 
                    self.animar(pantalla, "Derecha")
                self.caminar(pantalla)
            case "Izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "Izquierda")
                self.caminar(pantalla)
            case "Salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "Dispara":
                if direccion == "Derecha":
                    self.animar(pantalla, "Dispara")
                elif direccion == "Izquierda":
                    self.animar(pantalla, "Dispara_Izquierda")
            case "Quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "Quieto")
        self.aplicar_gravedad(pantalla, plataformas)


        self.actualizar_disparo(pantalla)
        self.verificar_coalision(lista_enemigos)

    
    def aplicar_gravedad(self, pantalla, plataformas):
        
        if self.esta_saltando:
            self.animar(pantalla, "Salta")
            self.rectangulo_principal.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

        for pl in plataformas:
            if not pl.premio:
                if self.rectangulo_principal.colliderect(pl.rectangulo):
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                    self.rectangulo_principal.bottom = pl.rectangulo.top + 2 
                    break
                else:
                    self.esta_saltando = True


    def disparar(self, pantalla, lista_enemigos, plataformas):

        x = None

        if self.direccion == "Derecha":
            x = self.rectangulo_principal.right - 50
        else:
            x = self.rectangulo_principal.left - 130

        # Crea un nuevo disparo
        self.disparo = Disparo(x, self.rectangulo_principal.y, r"img\jack\36.png", 50, pantalla, self.direccion)

        self.disparo.verificar_coalicion_enemigo(plataformas)

        if x is not None:
            self.lista_disparos.append(self.disparo)

        self.disparo.mover()
        
    
    def actualizar_disparo(self, pantalla):

        i = 0

        while i < len(self.lista_disparos):

            p = self.lista_disparos[i]

            p.mover()

            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_disparos.pop(i)

                i -= 1

            i += 1


    def verificar_coalision(self, lista_enemigos):
        i = 0

        while i < len(lista_enemigos):
            
            enemigo = lista_enemigos[i]

            if self.rectangulo_principal.colliderect(enemigo.rectangulo):
                
                self.vidas -= 1        
            
            i += 1

                