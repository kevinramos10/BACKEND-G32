class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("gua gua")
    
class Gato(Animal):
    def hacer_sonido(self):
        print("miau miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu")

#lista de instancias
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    #el mismo metodo tiene diferente resultado
    animal.hacer_sonido()


#El polimorfismo sirve para crear codigo mas generico indicando que siempre voy a tener ese metodo
#porque esta dentro de la familia y no voy a tener que validar que el metodo existe antes de llamarlo sea
#cual sea la clase

#Es la base de muchos patrones de diseño y de las librerias como Django Flask

