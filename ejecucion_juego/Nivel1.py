from Plantilla import *
import random
from Preguntas import*

preguntas = primer_nivel
respuestas_correctas = r_nivelUno
respuestas = []
jugadores = []
marcador = []

class Primer_Nivel(Juego):
    def __init__(self,preguntas, respuestas_correctas, respuestas, jugadores, marcador):
            super().__init__(preguntas, respuestas_correctas, respuestas, jugadores, marcador)
    

    def level1(self):
        p= 1
        puntaje = 0
        while p <=3:
            player = input(f"\nIngrese el nombre del jugador #{p}: ")
            self.jugadores.append(player)
            p+=1
            for i in range(3):
                print(f"\t{random.sample(self.preguntas,1)}\n")
                respuesta = input("").lower()
                self.respuestas.append(respuesta)
                if self.respuestas[i] in self.respuestas_correctas:
                    puntaje +=1
                else:
                    print("incorrecto")
            self.marcador.append(puntaje)
            self.respuestas = []
            puntaje = 0
            
        print("\t****MARCADOR GLOBAL****\n")
        for i in range(len(self.jugadores)):
            print(f"\t{self.jugadores[i]} = {self.marcador[i]} Puntos\n")
        print("\t****SEGUNDO NIVEL****")