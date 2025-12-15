class Pedido:
    def __init__(self, total):
        self.__total = total

    def mostrar(self):
        print(self.__total)

Pedido(500).mostrar()
