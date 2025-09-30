from datetime import datetime, date
from idlelib.pyshell import use_subprocess
from tkinter.font import names


class Logger:
    def __init__(self):
        self.logs = []

    def log(self, mensaje):
        self.logs.append(f"[{datetime.strftime(f'%Y-%m-%d %H:%M')}]")

    def shows_logs(self):
        return self.logs

class Usuario:
    def __init__(self, usuario_id, nombre):
        self.id = usuario_id
        self.nombre = nombre
        self.pedidos:list["Pedido"] = []
        self.logger = Logger()

    def registrar(self):
        self.logger.log(f'El usuario {self.nombre} se ha registrado')

    def agregar_pedido(self, pedido: 'Pedido'):
        self.pedidos.append(pedido)
        self.logger.log(f'El pedido {pedido_id} se agrego al usuario {self.id}')

    def get_pedidos(self):
        return self.pedidos

class Pedido:
    def __init__(self, pedido_int, fecha, monto):
        self.id = pedido_int
        self.fecha = fecha
        self.monto = monto
        self.estado = 'Pendiente'
        self.logger = Logger()

    def procesar(self):
        self.estado = 'Procesado'
        self.log(f'El pedido {self.id} se ha procesado')

    def cancelar(self):
        self.estado = 'Cancelado'
        self.logger.log(f'El pedido {self.id} se ha cancelado')

    def mostrar_detalles(self):
        return f'Pedido: {self.id} | Fecha: {self.fecha} | Monto: {self.monto}'

if __name__ == '__main__':
    usuario = Usuario(1, 'Fernandito')
    usuario.registrar()

    p1 = Pedido(101, date.today().strftime('%Y-%m-%d'), 4000)
    usuario.agregar_pedido(p1)
    p1.procesar()

    p2 = Pedido(101, date.today().strftime('%Y-%m-%d'), 4000)
    usuario.agregar_pedido(p2)
    p2.cancelar()

    print(f'Pedidos del usuario {usuario.nombre}')
    for pedido in usuario.get_pedidos():
        print(pedido.mostrar_detalles())

    print(f'Registros del usuario {usuario.nombre}')
    for pedido in usuario.get_pedidos():
        print(pedido.mostrar_detalles())

