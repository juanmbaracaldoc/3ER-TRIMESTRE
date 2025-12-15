class Auto:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    def acelerar(self):
        print(f"El auto {self.marca} acelera.")

auto = Auto("Rojo", "Toyota")
auto.acelerar()
