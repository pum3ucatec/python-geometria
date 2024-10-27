from geometria.geometria import Geometria

class Cuadrado(Geometria):
    def __init__(self, p1, lado, borde="black", relleno=""):
        self.p1 = p1  
        self.lado = lado
        self.borde = borde
        self.relleno = relleno

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

    def dibujar(self, canvas):
        x, y = self.p1.x, self.p1.y
        l = self.lado
        canvas.create_rectangle(x, y, x + l, y + l, outline=self.borde, fill=self.relleno)

        # Mostrar el área y el perímetro como texto
        canvas.create_text(x + l / 2, y + l + 20, text=f"Área: {self.calcular_area():.2f}")
        canvas.create_text(x + l / 2, y + l + 40, text=f"Perímetro: {self.calcular_perimetro():.2f}")
