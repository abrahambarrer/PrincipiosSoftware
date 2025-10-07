public class PayPalPago : IPago
{
    public void ProcesarPago(decimal monto)
    {
        Console.WriteLine($"Procesando pago con PayPal: ${monto}");
    }
    
    public bool ValidarPago()
    {
        Console.WriteLine("Validando cuenta PayPal...");
        return true;
    }
}