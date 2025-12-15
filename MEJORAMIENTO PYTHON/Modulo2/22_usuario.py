class Usuario:
    def __init__(self, user):
        self.__user = user

    def mostrar(self):
        print(self.__user)

Usuario("admin").mostrar()
