from draw_api.DrawAPI import DrawAPI

class DrawToSVF(DrawAPI):

    def __init__(self):
        self._svg_elements = []

    def comenzar_dibujo(self):
        self._svg_elements.append('')

    def terminar_dibujo(self):
        self._svg_elements.append('</svg>')
        with open('output.svg', 'w', encoding='utf-8') as f:
            f.write('\n'.join(self._svg_elements))

        print('SVG guardado')

    def dibujar_rectangulo(self, x, y, alto, ancho, color, alpha):
        self._svg_elements.append(f'<circle cx="{x}" cy="{y}" alto="{alto}" ancho="{ancho}" relleno="{color}" opacidad="{alpha}"/>')

    def dibujar_circulo(self, x, y, radio, color, alpha):
        self._svg_elements.append(f'<rect cx="{x}" cy="{y}" radio="{radio}" relleno="{color}" opacidad="{alpha}"/>')

