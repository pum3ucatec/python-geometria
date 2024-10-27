# src/geometria/circulo.py

import math
from geometria.geometria import Geometria

class Circulo(Geometria):
    def __init__(self,centro, radio, borde="black", relleno=""):
        self.centro = centro
        self.radio = radio
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def dibujar(self, canvas):
        x = self.centro.x
        y = self.centro.y
        r = self.radio
        canvas.create_oval(x -r, y - r, x + r, y + r, outline = "blue", fill = "lightblue")

        canvas.create_text(x, y + r + 20, text=f"Área: {self.calcular_area():.2f}")
        canvas.create_text(x, y + r + 40, text=f"Perímetro: {self.calcular_perimetro():.2f}")    