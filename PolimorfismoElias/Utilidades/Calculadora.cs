namespace TiposdePolimorfismo.Utilidades
{
    public class Calculadora
    {
        public int Sumar(int a, int b)
      {
          return a + b;
      }

      public static sumar operator +(numero1, numero2) 
      {
          return numero1 + numero2; 
      }

      public static Calculadora operator +(Calculadora c1, Calculadora c2)
      {
        return new Calculadora();
      }
    }
}