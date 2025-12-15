class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

cuenta = Cuenta(500)
cuenta.depositar(200)
print(cuenta.saldo)
