class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario

    def pagar(self):
        print(self.__salario)

Empleado("Carlos", 3000).pagar()
