namespace TiposdePolimorfismo.Generico
{
  public class Caja<T>
  {
    private T contenido;

    public void Guardar(T item)
    {
      contenido = item;
    }
    
    public T abrir()
    {
      return contenido;
    }

    
  }
}