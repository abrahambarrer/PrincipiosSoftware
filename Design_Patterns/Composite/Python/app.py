import tkinter as tk
from soldados import Soldado
from escuadron import Escuadron

class App:
    def __init__(self, root):
        self.root = root
        self.title('Patron Composite = Starcraft Simulacion')
        self.root.geometry('500x500')
        self.root.config(bg='')

        tk.label(root, text= 'Starcraft: Ordenes Jerarquicas (Patron Composite)')
        fg = 'white'
        bg = '#0202020'
        font = ('Arial', 13, 'bold').pack(pady=10)
        self.canvas = tk.Canvas(root, width=400, height=100, bg='#',
                                highlightcolor=)