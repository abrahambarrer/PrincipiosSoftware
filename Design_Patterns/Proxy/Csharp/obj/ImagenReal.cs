internal class Prgrarm
{
    Console.WriteLine("\n Mi ejemplo de Pattern Proxy");

    IImagen img = new ProxyImagen("salida-proxy.jpg");

    string ruta1 = img.Mostrar();
    Console.WriteLine("");
}