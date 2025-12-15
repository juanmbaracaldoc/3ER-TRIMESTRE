class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def leer(self):
        print(f"Leyendo {self.titulo}")

libro = Libro("1984", "Orwell")
libro.leer()
