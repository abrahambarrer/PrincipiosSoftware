using System;
using CineEnCasa.Subsistemas;
using CineEnCasa.Facade;

namespace CineEnCasa
{
    class Program 
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Configurando sistema de cine en casa...");

            Amplificadores amp = new Amplificador();
            ReproductorBlueRay br = new ReproductorBlueRay();
            Proyector proy = new Proyector();
            SistemaLuces luces = new SistemaLuces();

            CineEnCasaFacade cineEnCasa = new CineEnCasaFacade(amp, br);
        }
    }
}