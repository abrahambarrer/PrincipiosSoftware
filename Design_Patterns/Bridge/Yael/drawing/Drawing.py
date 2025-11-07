from shapes import Shape
from draw_api import DrawAPI
from typing import List

class Drawing:
    def __init__(self, draw_api: DrawAPI):
        self.draw_api = draw_api
        self.shapes: List[Shape] = []

    def añadir_figura(self, shape: Shape):
        self.shapes.append(shape)

    def render(self):
        self.draw_api.empezar_dibujo(self)
        for shape in self.shapes:
            shape.dibujar()
        self.draw_api.terminar_dibujo()

    def cambiar_render(self, nuevo_draw_api: DrawAPI):
        self.DrawAPI = nuevo_draw_api
        for shape in self.shapes:
            shape.drawAPI