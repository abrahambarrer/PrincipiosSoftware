from manejadordatos import ManejadorDatos

class Caja:
    def __init__(self, archivo):
        self.datos = ManejadorDatos(archivo)

    def vender(self, producto, cantidad):
        self.datos.actualizar(producto, -cantidad)
        self.guardar()