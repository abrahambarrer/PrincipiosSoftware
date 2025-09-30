using System;

namespace buenEjemplo
{
  public class Xiamoi12 : TelefonoBasico, DesbloqueoBiometrico
  {
    public Xiamoi12(string marca, int modelo, int precio, int RAM) : base(marca, modelo, precio, RAM)
    {
        
    }

    public override void escribir()
    {
      Console.WriteLine($"Escribiendo desde mi {marca}");
    }

    public override void llamar()
    {
      Console.WriteLine($"Llamando desde mi {marca}");
    }

    public void desbloquearConHuella()
    {
      Console.WriteLine($"Desbloqueando con huella desde mi {marca}");
    }
  }
}