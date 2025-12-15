class Carro:
    def __init__(self, marca, vmax):
        self.marca = marca
        self.__vmax = vmax

    def acelerar(self):
        print(self.__vmax)

Carro("BMW", 250).acelerar()
