using System.Drawing;

namespace CSHARDP_GEOMETRIA
{
    public class Circulo
    {
        private double CentroX;
        private double CentroY;
        private double Radio;
        private Color Borde;
        private Color Relleno;

        public Circulo(double centroX, double centroY, double radio, Color borde, Color relleno)
        {
            CentroX = centroX;
            CentroY = centroY;
            Radio = radio;
            Borde = borde;
            Relleno = relleno;
        }

        public double CalcularArea()
        {
            return Math.PI * (Radio * Radio);
        }

        public double CalcularPerimetro()
        {
            return 2 * Math.PI * Radio;
        }

        public void Dibujar(Graphics g)
        {
            using (Brush brush = new SolidBrush(Relleno))
            {
                g.FillEllipse(brush, (float)(CentroX - Radio), (float)(CentroY - Radio), (float)(Radio * 2), (float)(Radio * 2));
            }
            using (Pen pen = new Pen(Borde))
            {
                g.DrawEllipse(pen, (float)(CentroX - Radio), (float)(CentroY - Radio), (float)(Radio * 2), (float)(Radio * 2));
            }

            g.DrawString($"Área: {CalcularArea():F2}", SystemFonts.DefaultFont, Brushes.Black, (float)CentroX, (float)CentroY + (float)Radio + 5);
            g.DrawString($"Perímetro: {CalcularPerimetro():F2}", SystemFonts.DefaultFont, Brushes.Black, (float)CentroX, (float)CentroY + (float)Radio + 20);
        }
    }
}
