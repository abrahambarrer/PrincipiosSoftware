public class ProcesadorPagos
{
    public void ProcesarPago(string tipoPago, decimal monto)
    {
        IPago pago;
        
        // Lógica de creación DIRECTA sin factory
        if (tipoPago.ToLower() == "tarjeta")
        {
            pago = new TarjetaCreditoPago();
        }
        else if (tipoPago.ToLower() == "paypal")
        {
            pago = new PayPalPago();
        }
        else if (tipoPago.ToLower() == "transferencia")
        {
            pago = new TransferenciaPago();
        }
        else
        {
            throw new ArgumentException("Tipo de pago no soportado");
        }
        
        if (pago.ValidarPago())
        {
            pago.ProcesarPago(monto);
        }
    }
}