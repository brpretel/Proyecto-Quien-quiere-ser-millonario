from Nivel1 import*
from itertools import zip_longest
from Preguntas import*

preguntas2 = segundo_nivel
respuestas_correctas2 = r_nivelDos
respuestas2 = []
marcador_dos = []


class Segundo_Nivel(Primer_Nivel):
    def __init__(self, preguntas, respuestas_correctas, respuestas, jugadores, marcador,marcador_dos,preguntas2,respuestas_correctas2,respuestas2):
            super().__init__(preguntas, respuestas_correctas, respuestas, jugadores, marcador)
            self.marcador_dos = marcador_dos
            self.preguntas2 = preguntas2
            self.respuestas_correctas2 = respuestas_correctas2
            self.respuestas2 = respuestas2

    def level2(self,jugadores):
        p= 1
        j = 0
        puntaje = 0
        while p <=3:
            print(jugadores[j])
            p+=1
            j+=1
            for i in range(3):
                print(f"\t{random.sample(self.preguntas2,1)}\n")
                respuesta = input("").lower()
                self.respuestas2.append(respuesta)
                if self.respuestas2[i] in self.respuestas_correctas2:
                    puntaje +=1
                else:
                    print("incorrecto")
            self.marcador_dos.append(puntaje)
            self.respuestas2 = []
            puntaje = 0
        print("\t****MARCADOR GLOBAL****\n")
        result = [sum(n) for n in zip_longest(marcador, marcador_dos,)]
        for i in range(len(self.jugadores)):
            print(f"\t{self.jugadores[i]} = {result[i]} Puntos")