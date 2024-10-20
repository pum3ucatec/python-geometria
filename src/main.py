
import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.elipse import Elipse
from geometria.cuadrado import Cuadrado

def dibujar_rectangulo(canvas, rectangulo):
    x0 = 100
    y0 = 100
    x1 = x0 + rectangulo.ancho
    y1 = y0 + rectangulo.alto
    canvas.create_rectangle(x0, y0, x1, y1, outline="red", fill="lightcoral")

def dibujar_circulo(canvas, circulo):
    x = 400
    y = 100
    r = circulo.radio
    canvas.create_oval(x-r, y-r, x+r, y+r, outline="blue", fill="lightblue")
    
def dibujar_elipse(canvas, elipse):
    x = 200
    y = 300
    r1 = elipse.radio1
    r2 = elipse.radio2
    canvas.create_oval(x-r1, y-r2, x+r1, y+r2, outline="purple", fill="orange")
    
def dibujar_cuadrado(canvas, cuadrado):
    x0 = 400
    y0 = 250
    x1 = x0 + cuadrado.lado
    y1 = y0 + cuadrado.lado
    canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="yellow")

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # Crear objetos
    circulo = Circulo(58)
    rectangulo = Rectangulo(140, 90)
    elipse = Elipse(70,40)
    cuadrado = Cuadrado(75)
    
    # Dibujar
    dibujar_circulo(canvas, circulo)
    dibujar_rectangulo(canvas, rectangulo)
    dibujar_elipse(canvas, elipse)
    dibujar_cuadrado(canvas, cuadrado)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
