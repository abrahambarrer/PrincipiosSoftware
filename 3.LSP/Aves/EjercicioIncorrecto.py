from abc import ABC, abstractmethod

@abstractmethod
class Ave(ABC):
    def volar(self):
        pass
    def comer(self):
        pass
    def nadar(self):
        pass

class Aguila(Ave):
    def volar(self):
        print("Aguila esta volando...")
    def comer(self):
        print("Aguila esta comiendo...")
    def nadar(self):
        raise Exception("Las aguilas no nadan")

class Paloma(Ave):
    def volar(self):
        print("Paloma esta volando...")
    def comer(self):
        print("Paloma esta comiendo...")
    def nadar(self):
        raise Exception("Las palomas no nadan")

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pinguinos no vuelan")
    def comer(self):
        print("Pinguino esta comiendo...")
    def nadar(self):
        print("Pinguino esta nadando")

a1 = Aguila()
pa1 = Paloma()
pi1 = Pinguino()

a1.volar()
a1.comer()
a1.nadar()

pa1.volar()
pa1.comer()
pa1.nadar()

pi1.volar()
pi1.comer()
pi1.nadar()