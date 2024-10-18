import math
from geometria.geometria import Geometria
class Elipse(Geometria):
    def __init__(self, semi_eje_mayor, semi_eje_menor):
        self.semi_eje_mayor = semi_eje_mayor
        self.semi_eje_menor = semi_eje_menor

    def calcular_area(self):
        return math.pi * self.semi_eje_mayor * self.semi_eje_menor

    def calcular_perimetro(self):
        return math.pi * (3 * (self.semi_eje_mayor + self.semi_eje_menor) - 
                          math.sqrt((3 * self.semi_eje_mayor + self.semi_eje_menor) * 
                                     (self.semi_eje_mayor + 3 * self.semi_eje_menor)))