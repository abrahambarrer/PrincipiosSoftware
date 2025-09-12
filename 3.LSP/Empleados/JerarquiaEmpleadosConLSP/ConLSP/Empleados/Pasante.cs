using ConLSP.Interfaces;

namespace ConLSP.Empleados
{
    public class Pasante : IEmpleado
    {
        public string Nombre { get; }
        public string Puesto { get; } = "Pasante";

        private readonly ITrabajador _trabajador;
        
        public Pasante(string nombre, ITrabajador trajador)
        {
            Nombre = nombre;
            _trabajador = trajador;
        }

        public void Trabajar() => _trabajador.Trabajar();
    }
}
