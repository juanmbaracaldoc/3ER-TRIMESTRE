class Sensor:
    def __init__(self, valor):
        self.__valor = valor

    def leer(self):
        return self.__valor

print(Sensor(25).leer())
