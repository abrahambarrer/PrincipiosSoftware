using System;

namespace buenEjemplo  
{
  public abstrac class TelefonoBasico
  {
    public string marca;
    public int modelo;
    public int precio;
    public int RAM;

    public TelefonoBasico(string marca, int modelo, int precio, int RAM)
    {
      this.marca = marca;
      this.modelo = modelo;
      this.precio = precio;
      this.RAM = RAM;
    }
  }
}