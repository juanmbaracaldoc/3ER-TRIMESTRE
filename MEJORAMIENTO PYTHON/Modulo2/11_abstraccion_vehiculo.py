class Vehiculo:
    def mover(self):
        pass

class Auto(Vehiculo):
    def mover(self):
        print("Auto moviéndose")

Auto().mover()
