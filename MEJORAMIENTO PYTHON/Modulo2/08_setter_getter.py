class Persona:
    def __init__(self):
        self.__edad = 0

    def set_edad(self, e):
        if e >= 0:
            self.__edad = e

    def get_edad(self):
        return self.__edad

p = Persona()
p.set_edad(25)
print(p.get_edad())
