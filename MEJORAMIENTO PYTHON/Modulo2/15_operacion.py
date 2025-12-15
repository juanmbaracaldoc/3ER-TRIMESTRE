class Operacion:
    def ejecutar(self, a, b):
        pass

class Multiplicar(Operacion):
    def ejecutar(self, a, b):
        return a * b

print(Multiplicar().ejecutar(5, 4))
