# src/geometria/rectangulo.py

from geometria.geometria import Geometria
from geometria.punto import Punto
class Rectangulo(Geometria):
    def __init__(self, p1, p2, borde="black", relleno=""):
        self.punto_inicial = p1
        self.punto_final = p2
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        return 0

    def calcular_perimetro(self):
        return 0

    def dibujar(self, canvas):
        canvas.create_rectangle(self.punto_inicial.x, self.punto_inicial.y, self.punto_final.x, self.punto_final.y, outline=self.borde, fill=self.relleno)
