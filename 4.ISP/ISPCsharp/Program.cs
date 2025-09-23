using System;
using malEjemplo;
using buenEjemplo;

namespace Exposicion22
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hello World!");

      ZTE mizte = new ZTE("ZTE", 2019, 1000, 2);

      mizte.escribir();
      mizte.llamar();
      mizte.pagarConNFC();
      mizte.usarAsistenteVirtual();
      mizte.desbloquearConHuella()

      iphone15 miiphone = new iphone15("iphone15", 2023, 1000, 2);
      miiphone.escribir();
      miiphone.llamar();
      miiphone.pagarConNFC();
      miiphone.usarAsistenteVirtual();

      Xiamoi mixiaomi = new Xiamoi("Xiamoi", 2023, 1000, 2);
      mixiaomi.escribir();
      mixiaomi.llamar();
      mixiaomi.pagarConNFC();
      mixiaomi.usarAsistenteVirtual()
      mixiaomi.desbloquearConHuella()

      ZTE2 mizte2 = new ZTE2("ZTE2", 2023, 1000, 2);
      mizte2.escribir();
      mizte2.llamar()

      Xiamoi12 mixiaomi12 = new Xiamoi12("Xiamoi12", 2023, 1000, 2);
      mixiaomi12.escribir();
      mixiaomi12.llamar();

      Iphone16 miiphone16 = new iphone16("iphone16", 2023, 1000, 2);
      miiphone16.escribir();
      miiphone16.llamar();
    }
  }
}