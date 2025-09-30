using System;

namespace malEjemplo
{
  public class Xiamoi : Telefono
  {
    public Xiamoi(string marca, int modelo, int precio, int RAM) : base(marca, modelo, precio, RAM)
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

    public override void pagarConNFC()
    {
      Console.WriteLine($"Pagando con NFC desde mi {marca}");
    }

    public override void usarAsistenteVirtual()
    {
      Console.WriteLine("Este dispositivo no tiene acceso a esta funcion");
    }

    public override void desbloquearConHuella()
    {
      Console.WriteLine("Este dispositivo no tiene acceso a esta funcion")
    }
  }
}