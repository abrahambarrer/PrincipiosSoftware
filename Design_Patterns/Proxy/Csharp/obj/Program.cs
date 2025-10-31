using System;
using System.IO;

namespace ProxyImagenDemo
{
    internal class Program
    {
        private static Main(string[] args)
        {
            IImagen img = new ProxyImagen("salida-proxy.jpg");

            string ruta1 = img.Mostrar();
            Console.WriteLine("mostrando la imagen " + ruta1);

            Console.WriteLine("generando imagen otra vez");

            string ruta2 = img.Mostrar();
            Console.WriteLine("la imagen : " + ruta2);

            Console.WriteLine(" la imagen esta en la ruta" + Path.GetFullPath(ruta2));
        }
    }
}