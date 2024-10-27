import java.awt.Color;
import java.awt.Graphics;

public class Circulo {
    private final double centroX;
    private final double centroY;
    private final double radio;
    private final Color borde;
    private final Color relleno;

    public Circulo(double centroX, double centroY, double radio, Color borde, Color relleno) {
        this.centroX = centroX;
        this.centroY = centroY;
        this.radio = radio;
        this.borde = borde;
        this.relleno = relleno;
    }

    public double calcularArea() {
        return Math.PI * Math.pow(radio, 2);
    }

    public double calcularPerimetro() {
        return 2 * Math.PI * radio;
    }

    public void dibujar(Graphics g) {
        // Dibuja el relleno
        g.setColor(relleno);
        g.fillOval((int)(centroX - radio), (int)(centroY - radio), (int)(radio * 2), (int)(radio * 2));
        
        // Dibuja el borde
        g.setColor(borde);
        g.drawOval((int)(centroX - radio), (int)(centroY - radio), (int)(radio * 2), (int)(radio * 2));

        // Dibuja el área y el perímetro
        g.setColor(Color.BLACK);
        g.drawString(String.format("Área: %.2f", calcularArea()), (int)centroX, (int)(centroY + radio + 15));
        g.drawString(String.format("Perímetro: %.2f", calcularPerimetro()), (int)centroX, (int)(centroY + radio + 30));
    }
}
