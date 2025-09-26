from manejadordatos import ManejadorDatos


class Bodega:
    def __init__(self, archivo):
        self.datos = ManejadorDatos(archivo)

    def reabastecer(self, producto, cantidad):
        self.datos.actualizar(producto, cantidad)
        self.guardar()