from draw_api import DrawAPI
from shapes import Shape

class Rectangle(Shape):
    def __init__(self, x, y, ancho, alto, drawAPI, color='black', alpha=1.0):
        super().__init__(drawAPI, color, alpha)
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto

    def dibujar(self):
        self.drawAPI.drawRentangle(self.x, self.y, self.ancho, self.alto, self.color, self.alpha)

