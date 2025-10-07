using Factory;
using Producto;

class Program
{
    static void Main()
    {
        ProcesarPago(TipoPago.TarjetaCredito, 100.50);
        ProcesarPago(TipoPago.PayPal, 75.25);
        ProcesarPago(TipoPago.Transferencia, 200.00);
    }

    static void ProcesarPago(TipoPago tipo, decimal monto)
    {
        IPago pago = PagoFactory.crearPago(tipo);

        if(pago.ValidarPago())
        {
            pago.ProcesarPago(monto);
        }
    }
}