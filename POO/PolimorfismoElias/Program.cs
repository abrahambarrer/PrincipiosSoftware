using System;
using TiposdePolimorfismo.Figura;
using TiposdePolimorfismo.Utiidades;
using TiposdePolimorfismo.Unidades;
using TiposdePolimorfismo.Generico;

class Program
{
  public static void Program(string[] args)
  {
    List<Figura> figuras = new List<Figura>()
    {
      new Circulo(5)
      new Rectangulo(4, 6)
      new Circulo(3)
    };

    foreach (var figura in figuras)
    {
      figura.dibujar();
      Console.WriteLine("Area: " + figura.calcularaArea())
    }

    Caja<string> caja1 = new Caja<string>(10);
    caja1.guardar("Hola Mundo");
    Console.WriteLine(caja1.abrir())

    Caja<int> caja2 = new Caja<int>();
    caja2.guardar(123);
    Console.WriteLine("Contenido de la caja: " + caja2.abrir())

    Calculadora calc = new Calculadora();
    Console.WriteLine(calc.Sumar(5, 3))
    Console.WriteLine(calc.Sumar(5.5, 10.3))

    Metro metro = 10;
    double d = (double)metro;
    Console.WriteLine(metro)
    
  } 
}