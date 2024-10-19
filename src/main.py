
import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.punto import Punto

def dibujar_circulo(canvas, circulo):
    x = 100
    y = 100
    r = circulo.radio
    canvas.create_oval(x - r, y - r, x + r, y + r, outline="blue", fill="lightblue")

def dibujar_cuadrado(canvas, cuadrado):
    x0 = 350
    y0 = 150
    x1 = x0 + cuadrado.lado
    y1 = y0 + cuadrado.lado
    canvas.create_rectangle(x0, y0, x1, y1, outline="green", fill="green")

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # Crear objetos
    circulo = Circulo(50)
    rectangulo = Rectangulo(Punto(50, 50), Punto(150, 250), "blue", "red")

    rectangulo1 = Rectangulo(Punto(450, 250), Punto(100, 100))
    
    # Dibujar
    dibujar_circulo(canvas, circulo)
    rectangulo.dibujar(canvas)
    rectangulo1.dibujar(canvas)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
