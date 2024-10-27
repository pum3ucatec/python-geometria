import java.awt.*;

public class Rectangulo {
    private final double esquinaInferiorIzquierdaX;
    private final double esquinaInferiorIzquierdaY;
    private final double esquinaSuperiorDerechaX;
    private final double esquinaSuperiorDerechaY;
    private final Color borde;
    private final Color relleno;

    public Rectangulo(double p1X, double p1Y, double p2X, double p2Y, Color borde, Color relleno) {
        this.esquinaInferiorIzquierdaX = p1X;
        this.esquinaInferiorIzquierdaY = p1Y;
        this.esquinaSuperiorDerechaX = p2X;
        this.esquinaSuperiorDerechaY = p2Y;
        this.borde = borde;
        this.relleno = relleno;
    }

    public double calcularArea() {
        double ancho = esquinaSuperiorDerechaX - esquinaInferiorIzquierdaX;
        double alto = esquinaSuperiorDerechaY - esquinaInferiorIzquierdaY;
        return ancho * alto;
    }

    public double calcularPerimetro() {
        double ancho = esquinaSuperiorDerechaX - esquinaInferiorIzquierdaX;
        double alto = esquinaSuperiorDerechaY - esquinaInferiorIzquierdaY;
        return 2 * (ancho + alto);
    }

    public void dibujar(Graphics g) {
        g.setColor(relleno);
        g.fillRect((int) esquinaInferiorIzquierdaX, (int) esquinaInferiorIzquierdaY,
                (int) (esquinaSuperiorDerechaX - esquinaInferiorIzquierdaX),
                (int) (esquinaSuperiorDerechaY - esquinaInferiorIzquierdaY));
        g.setColor(borde);
        g.drawRect((int) esquinaInferiorIzquierdaX, (int) esquinaInferiorIzquierdaY,
                (int) (esquinaSuperiorDerechaX - esquinaInferiorIzquierdaX),
                (int) (esquinaSuperiorDerechaY - esquinaInferiorIzquierdaY));
        g.drawString("Área: " + String.format("%.2f", calcularArea()), (int) esquinaInferiorIzquierdaX, (int) esquinaSuperiorDerechaY + 15);
        g.drawString("Perímetro: " + String.format("%.2f", calcularPerimetro()), (int) esquinaInferiorIzquierdaX, (int) esquinaSuperiorDerechaY + 30);
    }
}
