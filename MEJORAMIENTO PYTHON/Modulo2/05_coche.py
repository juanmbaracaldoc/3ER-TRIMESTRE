class Coche:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print(self.marca, "arrancando")

Coche("Ford").arrancar()
