import math

from geometria.geometria import Geometria

class Elipse(Geometria):
    def __init__(self, eje_mayor, eje_menor):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def calcular_area(self):
        return math.pi * self.eje_mayor * self.eje_menor

    def calcular_perimetro(self):
        # Aproximación de Ramanujan para el perímetro de una elipse
        a = self.eje_mayor
        b = self.eje_menor
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
