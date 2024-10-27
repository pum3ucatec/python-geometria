
import tkinter as tk
from geometria.circulo import Circulo
from geometria.rectangulo import Rectangulo
from geometria.cuadrado import Cuadrado
from geometria.elipse import Elipse
from geometria.punto import punto

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Dibujo de Geometría")

    # Crear un lienzo
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # Crear objetos
    circulo = Circulo(punto(100,200),20, "blue", "black")
    rectangulo = Rectangulo(punto(300, 200), punto(350,250), "green", "red")
    cuadrado = Cuadrado(punto(100, 50),50, "yellow", "black") 
    elipse = Elipse(punto(300,100), 40, 30, "blue", "green")
    
    # Dibujar
    circulo.dibujar(canvas)
    rectangulo.dibujar(canvas)
    cuadrado.dibujar(canvas)
    elipse.dibujar(canvas)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
