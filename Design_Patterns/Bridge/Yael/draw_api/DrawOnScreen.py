from draw_api import DrawAPI


class DrawOnScreen(DrawAPI):

    def comenzar_dibujo(self):
        print('Dibujando en papel...')

    def terminar_dibujo(self):
        print('Terminando dibujo...')

    def dibujar_rectangulo(self, x, y, alto, ancho, color, alpha):
        print(f'Dibujo rectangulo en papel: {alto} x {ancho}, color: {color}, color')

    def dibujar_circulo(self, x, y, radio, color, alpha):
        print(f'Dibujo circulo en papel: radio: {radio}, color: {color}')