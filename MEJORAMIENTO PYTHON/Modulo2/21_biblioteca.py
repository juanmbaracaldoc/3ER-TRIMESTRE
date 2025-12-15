class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

b = Biblioteca()
b.agregar("Python")
print(b.libros)
