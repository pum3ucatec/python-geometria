import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.elipse import Elipse
from geometria.cuadrado import Cuadrado

def dibujar_rectangulo(canvas, rectangulo):
    x0 = 300
    y0 = 100
    x1 = x0 + rectangulo.ancho
    y1 = y0 + rectangulo.alto
    canvas.create_rectangle(x0, y0, x1, y1, outline="red", fill="lightcoral")

def dibujar_circulo(canvas, circulo):
    x = 100
    y = 100
    r = circulo.radio
    canvas.create_oval(x - r, y - r, x + r, y + r, outline="blue", fill="lightblue")

def dibujar_elipse(canvas, elipse):
    x = 450
    y = 350
    a = elipse.eje_mayor
    b = elipse.eje_menor
    canvas.create_oval(x - a, y - b, x + a, y + b, outline="green", fill="lightgreen")

def dibujar_cuadrado(canvas, cuadrado):
    x0 = 100
    y0 = 300
    x1 = x0 + cuadrado.lado
    y1 = y0 + cuadrado.lado
    canvas.create_rectangle(x0, y0, x1, y1, outline="purple", fill="lavender")

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # Crear objetos
    circulo = Circulo(50)
    rectangulo = Rectangulo(150, 100)
    elipse = Elipse(80, 50)
    cuadrado = Cuadrado(70)
    
    # Dibujar
    dibujar_circulo(canvas, circulo)
    dibujar_rectangulo(canvas, rectangulo)
    dibujar_elipse(canvas, elipse)
    dibujar_cuadrado(canvas, cuadrado)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
