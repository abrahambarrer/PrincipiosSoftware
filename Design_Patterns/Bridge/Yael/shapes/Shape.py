from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, drawAPI, color='black', alpha=1.0):
        self.drawAPI = drawAPI
        self.color= color
        self.alpha = alpha

    @abstractmethod
    def dibujar(self):
        pass
