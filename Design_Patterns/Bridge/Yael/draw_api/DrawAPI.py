from abc import ABC, abstractmethod
from binascii import a2b_base64


class DrawAPI(abc):

    @abstractmethod
    def dibujar_circulo(self, x, y, radio, color, alpha):
        pass

    @abstractmethod
    def dibujar_rectangulo(self, x, y, alto, ancho, color, alpha):
        pass

    @abstractmethod
    def empezar_dibujo(self, x, y, alto, ancho, color, alpha):
        pass

    @abstractmethod
    def terminar_dibujo(self):
        pass