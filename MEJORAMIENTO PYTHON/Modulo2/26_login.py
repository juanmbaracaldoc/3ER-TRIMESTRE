class Login:
    def __init__(self, clave):
        self.__clave = clave

    def validar(self, intento):
        print(intento == self.__clave)

Login("123").validar("123")
