class Producto:
    def __init__(self, precio):
        self.__precio = precio

    def get_precio(self):
        return self.__precio

print(Producto(500).get_precio())
