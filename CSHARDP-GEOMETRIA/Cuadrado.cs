using System.Drawing;

namespace CSHARDP_GEOMETRIA
{
    public class Cuadrado
    {
        private float P1; // Esquina superior izquierda X
        private float P2; // Esquina superior izquierda Y
        private float Lado;
        private Color Borde;
        private Color Relleno;

        public Cuadrado(float p1, float p2, float lado, Color borde, Color relleno)
        {
            P1 = p1;
            P2 = p2;
            Lado = lado;
            Borde = borde;
            Relleno = relleno;
        }

        public float CalcularArea()
        {
            return Lado * Lado;
        }

        public float CalcularPerimetro()
        {
            return 4 * Lado;
        }

        public void Dibujar(Graphics g)
        {
            using (Brush brush = new SolidBrush(Relleno))
            {
                g.FillRectangle(brush, P1, P2, Lado, Lado);
            }
            using (Pen pen = new Pen(Borde))
            {
                g.DrawRectangle(pen, P1, P2, Lado, Lado);
            }

            g.DrawString($"Área: {CalcularArea():F2}", SystemFonts.DefaultFont, Brushes.Black, P1, P2 + Lado + 5);
            g.DrawString($"Perímetro: {CalcularPerimetro():F2}", SystemFonts.DefaultFont, Brushes.Black, P1, P2 + Lado + 20);
        }
    }
}
