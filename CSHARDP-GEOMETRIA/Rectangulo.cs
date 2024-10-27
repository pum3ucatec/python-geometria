using System.Drawing;

namespace CSHARDP_GEOMETRIA
{
    public class Rectangulo
    {
        private float P1X; // Esquina Inferior Izquierda X
        private float P1Y; // Esquina Inferior Izquierda Y
        private float P2X; // Esquina Superior Derecha X
        private float P2Y; // Esquina Superior Derecha Y
        private Color Borde;
        private Color Relleno;

        public Rectangulo(float p1X, float p1Y, float p2X, float p2Y, Color borde, Color relleno)
        {
            P1X = p1X;
            P1Y = p1Y;
            P2X = p2X;
            P2Y = p2Y;
            Borde = borde;
            Relleno = relleno;
        }

        public float CalcularArea()
        {
            float ancho = P2X - P1X;
            float alto = P2Y - P1Y;
            return ancho * alto;
        }

        public float CalcularPerimetro()
        {
            float ancho = P2X - P1X;
            float alto = P2Y - P1Y;
            return 2 * (ancho + alto);
        }

        public void Dibujar(Graphics g)
        {
            using (Brush brush = new SolidBrush(Relleno))
            {
                g.FillRectangle(brush, P1X, P1Y, P2X - P1X, P2Y - P1Y);
            }
            using (Pen pen = new Pen(Borde))
            {
                g.DrawRectangle(pen, P1X, P1Y, P2X - P1X, P2Y - P1Y);
            }

            g.DrawString($"Área: {CalcularArea():F2}", SystemFonts.DefaultFont, Brushes.Black, P1X, P2Y + 5);
            g.DrawString($"Perímetro: {CalcularPerimetro():F2}", SystemFonts.DefaultFont, Brushes.Black, P1X, P2Y + 20);
        }
    }
}
