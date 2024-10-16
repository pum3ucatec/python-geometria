# src/geometria/circulo.py

import math
from geometria.geometria import Geometria

class Circulo(Geometria):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
