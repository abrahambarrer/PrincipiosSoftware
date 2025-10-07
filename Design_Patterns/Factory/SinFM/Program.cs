class Program
{
    static void Main()
    {
        var procesador = new ProcesadorPagos();
        
        // Uso directo - el cliente conoce los tipos concretos
        procesador.ProcesarPago("tarjeta", 100.50m);
        procesador.ProcesarPago("paypal", 75.25m);
        procesador.ProcesarPago("transferencia", 200.00m);
        
        // También se pueden crear directamente
        IPago pagoDirecto = new TarjetaCreditoPago();
        pagoDirecto.ProcesarPago(50.00m);
    }
}