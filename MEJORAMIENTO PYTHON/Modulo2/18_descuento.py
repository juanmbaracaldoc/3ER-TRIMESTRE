class Producto:
    def __init__(self, precio):
        self.__precio = precio

    def descuento(self, p):
        self.__precio -= self.__precio * p / 100
        print(self.__precio)

Producto(100).descuento(10)
