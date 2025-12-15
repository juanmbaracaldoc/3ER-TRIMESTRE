class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota

    def mostrar(self):
        print(self.__nota)

Estudiante("Ana", 4.5).mostrar()
