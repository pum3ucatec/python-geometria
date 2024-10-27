import java.awt.*;

public class Elipse {
    private final double centroX;
    private final double centroY;
    private final double ancho;
    private final double alto;
    private final Color borde;
    private final Color relleno;

    public Elipse(double centroX, double centroY, double ancho, double alto, Color borde, Color relleno) {
        this.centroX = centroX;
        this.centroY = centroY;
        this.ancho = ancho;
        this.alto = alto;
        this.borde = borde;
        this.relleno = relleno;
    }

    public double calcularArea() {
        return Math.PI * (ancho / 2) * (alto / 2);
    }

    public double calcularPerimetro() {
        return Math.PI * (3 * (ancho / 2 + alto / 2) - Math.sqrt((3 * (ancho / 2) + (alto / 2)) * ((ancho / 2) + 3 * (alto / 2))));
    }

    public void dibujar(Graphics g) {
        g.setColor(relleno);
        g.fillOval((int) (centroX - ancho / 2), (int) (centroY - alto / 2), (int) ancho, (int) alto);
        g.setColor(borde);
        g.drawOval((int) (centroX - ancho / 2), (int) (centroY - alto / 2), (int) ancho, (int) alto);
        g.drawString("Área: " + String.format("%.2f", calcularArea()), (int) centroX, (int) centroY + (int) (alto / 2) + 15);
        g.drawString("Perímetro: " + String.format("%.2f", calcularPerimetro()), (int) centroX, (int) centroY + (int) (alto / 2) + 30);
    }
}
