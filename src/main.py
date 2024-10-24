
import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.punto import Punto
from geometria.cuadrado import Cuadrado
from geometria.elipse import Elipse
def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=900, height=700)
    canvas.pack()

    # Crear objetos
    circulo = Circulo(Punto(350, 500), 50, relleno="#367380")
    rectangulo = Rectangulo(Punto(100, 100), Punto(300, 400), "blue", "red")
    cuadrado = Cuadrado(Punto(400, 100), 150, "Blue", "black")
    elipse = Elipse(Punto(600, 400), 120, 60, relleno="green", borde="black")


    
    resultado_label = tk.Label(root, text="", font=("Arial", 14))
    resultado_label.pack(pady=1)
    area = rectangulo.calcular_area()
    perimetro = rectangulo.calcular_perimetro()
    resultado_label.config(text=f"Área de Rectangulo: {area}, Perímetro: {perimetro}")


    resultado_label = tk.Label(root, text="", font=("Arial", 18))
    resultado_label.pack(pady=2)
    area = cuadrado.calcular_area()
    perimetro = cuadrado.calcular_perimetro()
    resultado_label.config(text=f"Área de cuadrado: {area}, Perímetro: {perimetro}")



    resultado_label = tk.Label(root, text="", font=("Arial", 22))
    resultado_label.pack(pady=3)
    area = elipse.calcular_area()
    perimetro = elipse.calcular_perimetro()
    resultado_label.config(text=f"Radio de elipse: {area:.2f}, Perímetro: {perimetro:.2f}")   

    
    resultado_label = tk.Label(root, text="", font=("Arial", 20),justify=tk.LEFT)
    resultado_label.pack(pady=4)
    area = circulo.calcular_area()
    perimetro = circulo.calcular_perimetro()
    resultado_label.config(text=f"""Área del círculo: {area:.2f} unidades cuadradasPerímetro del círculo: {perimetro:.2f} unidades""")

    

    # Dibujar
    circulo.dibujar(canvas)
    rectangulo.dibujar(canvas)
    cuadrado.dibujar(canvas)
    elipse.dibujar(canvas)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()