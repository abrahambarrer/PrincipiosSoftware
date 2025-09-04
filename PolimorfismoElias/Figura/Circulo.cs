namespace TiposdePolimorfismo.Figura
{
  public class Circulo : Figura
  {
    public double radio;

    public Circulo(double radio)
    {
      this.radio = radio;
    }

    public override double calcularaArea()
    {
      return Math.PI * radio * radio
    }

    public abstract void dibujar()
    {
      Console.WriteLine("Dibujando circulo con radio" + radio)
    }
  }
}