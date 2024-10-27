# src/geometria/rectangulo.py

from geometria.geometria import Geometria

class Rectangulo(Geometria):
    def __init__(self, p1, p2, borde, relleno):
        self.punto_inicial = p1
        self.punto_final = p2
        self.borde = borde
        self.relleno = relleno
        self.ancho = abs(self.punto_final.x - self.punto_inicial.x)
        self.alto = abs(self.punto_final.y - self.punto_inicial.y)

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def dibujar(self, canvas):
        canvas.create_rectangle(self.punto_inicial.x, self.punto_inicial.y, 
        self.punto_final.x,self.punto_final.y, outline=self.borde, fill=self.relleno)
    
        centro_x = (self.punto_inicial.x + self.punto_final.x) / 2
        parte_inferior_y = max(self.punto_inicial.y, self.punto_final.y)

        # Mostrar el área y el perímetro como texto
        canvas.create_text(centro_x, parte_inferior_y + 20, text=f"Área: {self.calcular_area():.2f}")
        canvas.create_text(centro_x, parte_inferior_y + 40, text=f"Perímetro: {self.calcular_perimetro():.2f}")