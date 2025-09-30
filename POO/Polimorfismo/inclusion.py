class Animal:
    def hablar(self):
        raise NotImplementedError ('Funcion no implementada')

class Perro(Animal):
    def hablar(self): return 'Guau'

class Gato(Animal):
    def hablar(self): return 'Miau'

def saludar(animal):
    print(animal.hablar())

saludar(Perro())
saludar(Gato())

