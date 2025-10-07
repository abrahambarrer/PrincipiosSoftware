public interface IPago
{
    void ProcesarPago(decimal monto);
    bool ValidarPago();
}
