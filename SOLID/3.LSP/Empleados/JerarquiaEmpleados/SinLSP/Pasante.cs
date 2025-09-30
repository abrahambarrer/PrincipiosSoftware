using System;

namespace SinLSP;

public class Pasante : Empleado
{
    public override decimal CalcularSalario()
    {
        throw new NotImplementeException("Los pasantes no reciben salario");
    }

    public override void Trabajar()
    {
        Console.WriteLine("Aprendiendo y ayudando");
    }


}