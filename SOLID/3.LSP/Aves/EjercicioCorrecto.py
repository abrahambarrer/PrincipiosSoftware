from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def comer(self):
        pass
    def respirar(self):
        pass

class AveVoladora(Ave):
    def volar(self):
        @abstractmethod
        def volaR(self):
            pass

class AveNadadora(Ave):
    @abstractmethod
    def nadar(self):
        pass

class Aguila(Ave):
    def comer(self):
        print('Aguila esta comiendo')
    def respirar(self):
        print('Aguila esta respirando')
    def volar(self):
        print('Aguila esta volando')

class Paloma(AveVoladora):
    def comer(self):
        print('Paloma esta comiendo')
    def respirar(self):
        print('Paloma esta respirando')
    def volar(self):
        print('Paloma esta volando')

class Pinguino(AveNadadora):
    def comer(self):
        print('Pinguino esta comiendo')
    def respirar(self):
        print('Pinguino esta respirando')
    def nadar(self):
        print('Pinguino esta nadando')

a1 = Aguila()
pa1 = Paloma()
pi1 = Pinguino()

a1.comer()
pa1.volar()
pi1.nadar()