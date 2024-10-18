# src/geometria/cuadrado.py

from geometria.geometria import Geometria

class Cuadrado(Geometria):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * (self.lado)
