import math

from geometria.geometria import Geometria

class Cuadrado(Geometria):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado