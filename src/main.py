
import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.punto import Punto

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    # Crear objetos
    circulo = Circulo(Punto(350, 550), 20, relleno="#367380")
    rectangulo = Rectangulo(Punto(50, 50), Punto(150, 250), "blue", "red")
    rectangulo1 = Rectangulo(Punto(450, 250), Punto(100, 100))
    
    resultado_label = tk.Label(root, text="", font=("Arial", 14))
    resultado_label.pack(pady=80)
    area = rectangulo.calcular_area()
    perimetro = rectangulo.calcular_perimetro()
    resultado_label.config(text=f"Área: {area}, Perímetro: {perimetro}")

    # Dibujar
    circulo.dibujar(canvas)
    rectangulo.dibujar(canvas)
    rectangulo1.dibujar(canvas)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
