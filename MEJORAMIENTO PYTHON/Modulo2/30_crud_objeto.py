class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

usuarios = []

usuarios.append(Usuario("Juan"))
print(usuarios[0].nombre)
