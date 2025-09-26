import datetime
from tkinter.font import names


class Logger:
    _instance = None
    _log:list[str] = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def log(self, mensaje):
        self._log.append((f'[{datetime.now().strftime('%Y-%m-%d %H:%M')}]'))

class Usuario:
    def __init__(self, usuario_id, nombre):
        self.id = usuario_id
        self.nombre = nombre
        self.pedidos:list['Pedido'] = []

    def registrar(self):
        logger = Logger()
        logger.log(f'El usuario {self.nombre} se ha registrado')

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
        logger = Logger()
        logger.log(f'El pedido {pedido.id} se agrego al usuario {self.nombre}')


class Pedido:
    def __init__(self, pedido_id, fecha, monto):
        self.id = pedido_id
        self.fecha = fecha
        self.monto = monto
        self.estado = 'Pendiente'

    def procesar(self):
        self.estado = 'Procesado'
        logger = Logger()
        logger.log(f'El pedido {self.id} se ha procesado')

    def cancelar(self):
        self.estado = 'Cancelado'
        logger = Logger()
        logger.log(f'El pedido {self.id} se ha cancelado')

    def mostrar_detalles(self):
        return f'Pedido: {self.id} | Fecha {self.fecha} | Monto: {self.monto} | Estado: {self.estado}'

if __name__ == '__main__':
    usuario = Usuario(1, 'Fernandito')
    usuario.registrar()

    p1 = Pedido(101, date.today().strftime('%Y-%m-%d'), 1000)
    usuario.agregar_pedido(p1)
    p1.procesar()

    p2 = Pedido(101, date.today().strftime('%Y-%m-%d'), 1000)
    usuario.agregar_pedido(p2)
    p2.procesar()

    print(f'Pedidos del usuario {usuario.nombre}: ')
    for pedido in usuario.get_pedidos():
        print(pedido.mostrar_detalles())

    pago_de_jesus = Logger()

    print('Registros del sistema: ')
    