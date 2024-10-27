import math
from geometria.geometria import Geometria

class Elipse(Geometria):
    def __init__(self, centro, radio_mayor, radio_menor, borde="black", relleno=""):
        self.centro = centro
        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        return math.pi * self.radio_mayor * self.radio_menor

    def calcular_perimetro(self):
        # Aproximación de Ramanujan para el perímetro de una elipse
        a, b = self.radio_mayor, self.radio_menor
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
    
    def dibujar(self, canvas):
        x, y = self.centro.x, self.centro.y
        rm, rn = self.radio_mayor, self.radio_menor
        canvas.create_oval(x - rm, y - rn, x + rm, y + rn, outline=self.borde, fill=self.relleno)

        # Mostrar el área y el perímetro como texto
        canvas.create_text(x, y + rn + 20, text=f"Área: {self.calcular_area():.2f}")
        canvas.create_text(x, y + rn + 40, text=f"Perímetro: {self.calcular_perimetro():.2f}")
