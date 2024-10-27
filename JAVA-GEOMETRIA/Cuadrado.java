import java.awt.*;

public class Cuadrado {
    private final double esquinaX;
    private final double esquinaY;
    private final double lado;
    private final Color borde;
    private final Color relleno;

    public Cuadrado(double x, double y, double lado, Color borde, Color relleno) {
        this.esquinaX = x;
        this.esquinaY = y;
        this.lado = lado;
        this.borde = borde;
        this.relleno = relleno;
    }

    public double calcularArea() {
        return lado * lado;
    }

    public double calcularPerimetro() {
        return 4 * lado;
    }

    public void dibujar(Graphics g) {
        g.setColor(relleno);
        g.fillRect((int) esquinaX, (int) esquinaY, (int) lado, (int) lado);
        g.setColor(borde);
        g.drawRect((int) esquinaX, (int) esquinaY, (int) lado, (int) lado);
        g.drawString("Área: " + String.format("%.2f", calcularArea()), (int) esquinaX, (int) esquinaY + (int) lado + 15);
        g.drawString("Perímetro: " + String.format("%.2f", calcularPerimetro()), (int) esquinaX, (int) esquinaY + (int) lado + 30);
    }
}
