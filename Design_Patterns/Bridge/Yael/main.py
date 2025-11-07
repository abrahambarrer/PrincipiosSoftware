from draw_api import DrawOnScreen, DrawOnPaper, DrawToSVG
from shapes import Circle, Rectangle
from drawing import Drawing

if __name__ == '__main__':
    pantall = DrawOnScreen
    papel = DrawOnPaper
    svg = DrawToSVG

    circulo = Circle(100, 100, 50, pantall, color='red', alpha=0.8)
    rectangulo = Rectangle(100, 100, 80, 40, pantall, color='red', alpha=0.8)

    dibujar = Drawing(pantall)
    dibujar.añadir_figura(rectangulo)

    print('\n Dibujo pantalla')
    dibujar.render()

    print('\n Dibujo papel')
    dibujar.cambiar_render(papel)

    print('\n Dibujo SVG')
    dibujar.cambiar_render(svg)