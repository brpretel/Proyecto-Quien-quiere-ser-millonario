from Nivel1 import*
from Nivel2 import*

def run():
    nivel1 = Primer_Nivel(preguntas,respuestas_correctas,respuestas,jugadores,marcador)
    nivel1.level1()
    nivel2 = Segundo_Nivel(preguntas, respuestas_correctas, respuestas, jugadores, marcador,marcador_dos,preguntas2,respuestas_correctas2,respuestas2)
    nivel2.level2(jugadores)


if __name__=="__main__":
    run()