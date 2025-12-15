class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def ver_saldo(self):
        return self.__saldo

print(Cuenta(1000).ver_saldo())
