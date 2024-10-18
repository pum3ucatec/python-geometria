# src/geometria/elipse.py

import math
from geometria.geometria import Geometria

class Elipse(Geometria):
    def __init__(self, radio1, radio2):
        self.radio1 = radio1
        self.radio2 = radio2
       
    def calcular_area(self):
        return math.pi * (self.radio1 * self.radio2)

# aproximación del perímetro por Ramanujan
    def calcular_perimetro(self):
        return math.pi*(3*(self.radio1+self.radio2)-((3*self.radio1+self.radio2)*(self.radio1+3*self.radio2))**(1/2))