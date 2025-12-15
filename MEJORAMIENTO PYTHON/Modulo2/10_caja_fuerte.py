class CajaFuerte:
    def __init__(self, pin):
        self.__pin = pin

    def abrir(self, intento):
        if intento == self.__pin:
            print("Caja abierta")
        else:
            print("Pin incorrecto")

CajaFuerte("1234").abrir("1234")
