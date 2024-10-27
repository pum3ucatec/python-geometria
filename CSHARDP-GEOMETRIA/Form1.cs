using System.Drawing;
using System.Windows.Forms;

namespace CSHARDP_GEOMETRIA
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            this.Text = "Dibujo de Geometría";
            this.ClientSize = new Size(600, 400);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            Graphics g = e.Graphics;

            // Crear objetos
            Circulo circulo = new Circulo(100, 200, 20, Color.Blue, Color.LightBlue);
            Rectangulo rectangulo = new Rectangulo(300, 200, 350, 250, Color.Green, Color.Red);
            Elipse elipse = new Elipse(200, 100, 40, 20, Color.Purple, Color.MistyRose);
            Cuadrado cuadrado = new Cuadrado(400, 200, 30, Color.Orange, Color.Yellow);

            // Dibujar
            circulo.Dibujar(g);
            rectangulo.Dibujar(g);
            elipse.Dibujar(g);
            cuadrado.Dibujar(g);
        }
    }
}
