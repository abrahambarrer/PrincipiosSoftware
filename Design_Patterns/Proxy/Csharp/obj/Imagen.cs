namespace
{
    public interface ProxyImagen : IImagen
    {
        private readonly string _rutaArchivo;
    }

    public string Mostrar()
    {
        if (_real == null)
        {
            _real = new ImagenReal(_rutaArchivo);
        }
        Console.WriteLine("[Proxy] ha dado acceso");
        Console.WriteLine("usando la imagen real ...");
        return _rutaArchivo = _rutaArchivo;
    }
}