from configuraciones import *

class Enemigo: 
    
    def __init__(self, animaciones) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, 60, 120)
        self.rectangulo = self.animaciones["Derecha"][0].get_rect()
        self.rectangulo.x = 600 #pos x
        self.rectangulo.y =  180 #pos Y
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Derecha"]


        self.esta_muerto = False
        self.esta_muriendo = False
        self.destino_x_band = False


    def avanzar(self):

        self.destino_x = 900

        # Obtener la diferencia entre la posición actual y el destino
        diferencia_x = self.destino_x - self.rectangulo.x

        if diferencia_x > 280:
            self.destino_x_band = False

        # Si la diferencia es mayor que cero, el enemigo se está moviendo hacia la derecha
        if diferencia_x > 0 and self.destino_x_band == False:
            self.destino_x_band = False
            self.rectangulo.x += 15
            self.animacion_actual = self.animaciones["Derecha"]


        # Si la diferencia es menor que cero, el enemigo se está moviendo hacia la izquierda
        elif diferencia_x <= 0 or self.destino_x_band == True:
            self.destino_x_band = True
            self.rectangulo.x -= 15
            self.animacion_actual = self.animaciones["Izquierda"]



            

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos +=1

        if self.esta_muriendo and self.contador_pasos == largo:
            self.esta_muerto = True
#setter de animacion actual

    def actualizar(self, pantalla):
        if not self.esta_muerto and not self.esta_muerto:
            self.animar(pantalla)
            self.avanzar()

    @staticmethod
    def crear_lista(piso):
        lista = []
        dict_enemigo = {}
        dict_enemigo["Derecha"] = enemigo_camina
        dict_enemigo["Izquierda"] = enemigo_camina_izquierda
        dict_enemigo["Disparo"] = enemigo_herida
        mi_enemigo = Enemigo(dict_enemigo)

        lista = [mi_enemigo]
        
        return lista
    

