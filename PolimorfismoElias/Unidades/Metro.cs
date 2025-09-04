namespace TiposdePolimorfismo.Unidades
{
  public class Metro
  {
    private double Valor {set; get;}
    
    public Metro(double valor)
    {
      Valor = valor;
    }

    public static explicit operator double(Metro m)
    {
      return m.Valor;
    }

    public static implicit operator Metro(double d)
    {
      return new Metro(d);
    }
  }
}