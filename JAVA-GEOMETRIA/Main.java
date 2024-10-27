import java.awt.*;
import javax.swing.*;

public class Main extends JPanel {

    private final Cuadrado cuadrado;
    private final Elipse elipse;
    private final Rectangulo rectangulo;
    private final Circulo circulo; 

    public Main() {
        cuadrado = new Cuadrado(50, 50, 100, Color.BLACK, Color.RED);
        elipse = new Elipse(250, 100, 150, 100, Color.BLACK, Color.GREEN);
        rectangulo = new Rectangulo(50, 200, 200, 300, Color.BLACK, Color.YELLOW);
        circulo = new Circulo(290, 250, 50, Color.BLACK, Color.ORANGE); // Inicializamos el círculo
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        cuadrado.dibujar(g);
        elipse.dibujar(g);
        rectangulo.dibujar(g);
        circulo.dibujar(g); // 
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Geometría");
        Main mainPanel = new Main();
        frame.add(mainPanel);
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
