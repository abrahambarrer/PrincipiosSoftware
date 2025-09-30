class Animal:
    def hablar(self):
        raise NotImplementedError ('Funcion no implementada')

class Perro(Animal):
    def hablar(self): return 'Guau'

class Gato(Animal):
    def hablar(self): return 'Miau'

class Caja:
    def __init__(self):
        self._items = []

    def meter(self, x):
        self._items.append(x)

    def primero(self):
        return self._items[0]

def saludar(animal):
    print(animal.hablar())

saludar(Perro())
saludar(Gato())

c1 = Caja()
c2 = Caja()
c1.meter(Perro())
c2.meter(Gato())

print(c1.primero().hablar())
print(c2.primero().hablar())