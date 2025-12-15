class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(self.nombre, self.edad)

Persona("Ana", 30).presentarse()
