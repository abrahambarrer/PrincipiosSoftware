from draw_api import DrawAPI
from shapes import Shape

class Circle(Shape):
    def __init__(self, x, y, radio, drawAPI, color='black', alpha=1.0):
        super().__init__(drawAPI, color, alpha)
        self.x = x
        self.y = y
        self.radio = radio

    def dibujar(self):
        self.drawAPI.drawCircle(self.x, self.y, self.radio, self.color, self.alpha)

