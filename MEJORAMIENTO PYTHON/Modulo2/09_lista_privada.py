class Lista:
    def __init__(self):
        self.__datos = []

    def agregar(self, d):
        self.__datos.append(d)

    def mostrar(self):
        return self.__datos

l = Lista()
l.agregar(1)
l.agregar(2)
print(l.mostrar())
