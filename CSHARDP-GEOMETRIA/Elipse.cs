using System.Drawing;

namespace CSHARDP_GEOMETRIA
{
    public class Elipse
    {
        private float Cx; // Centro X
        private float Cy; // Centro Y
        private float Ancho;
        private float Alto;
        private Color Borde;
        private Color Relleno;

        public Elipse(float cx, float cy, float ancho, float alto, Color borde, Color relleno)
        {
            Cx = cx;
            Cy = cy;
            Ancho = ancho;
            Alto = alto;
            Borde = borde;
            Relleno = relleno;
        }

        public float CalcularArea()
        {
            return (float)(Math.PI * (Ancho / 2) * (Alto / 2));
        }

        public float CalcularPerimetro()
        {
            return (float)(Math.PI * (3 * (Ancho / 2 + Alto / 2) - Math.Sqrt((3 * (Ancho / 2) + (Alto / 2)) * ((Ancho / 2) + 3 * (Alto / 2)))));
        }

        public void Dibujar(Graphics g)
        {
            using (Brush brush = new SolidBrush(Relleno))
            {
                g.FillEllipse(brush, Cx - Ancho / 2, Cy - Alto / 2, Ancho, Alto);
            }
            using (Pen pen = new Pen(Borde))
            {
                g.DrawEllipse(pen, Cx - Ancho / 2, Cy - Alto / 2, Ancho, Alto);
            }

            g.DrawString($"Área: {CalcularArea():F2}", SystemFonts.DefaultFont, Brushes.Black, Cx, Cy + (Alto / 2) + 5);
            g.DrawString($"Perímetro: {CalcularPerimetro():F2}", SystemFonts.DefaultFont, Brushes.Black, Cx, Cy + (Alto / 2) + 20);
        }
    }
}
