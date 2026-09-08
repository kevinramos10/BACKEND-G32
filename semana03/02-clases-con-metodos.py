#Las clases siempre empizan con mayusculas las primeras letras
class Mueble:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def dimensiones(self):
        print(f"Las dimensiones son: Largo: {self.largo}, Ancho: {self.ancho}, alto: {self.largo}")

m1 = Mueble(1.4, 0.7, 1.2)
m1.dimensiones()
#Si no se le pasa el self como parametro, ese metodo solo podra ser accedido directo desde la clase
#Es decir sin instacias
m1.largo = 10
m1.dimensiones()

#1. Ejercicio
#Crear una clase reectangulo en la cual tengamos en el constructor
#la base y la altura y tener un metodo para calcular su area calcular_area en la cual retorne
#el area el area del rectactagulo es base * altura

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print(f"El area es: {area}")

rect1 = Rectangulo(10,2)
rect1.calcular_area()

#2. crear una clase estudiante el cual tenga el atributo:
#nombre, notas, correo que deber ser inicializados el nombre y el correo
#y tengas su metodo agregar_nota(), tambien su metodo promedio() que me de el 
#promedio de todas las notas y el metodo estado que me de su estado si esta 

class Estudiante:
    def __init__(self, nombre, correo):
        self.nombre = nombre        
        self.correo = correo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio_notas(self):
        prom = 0
        for pro in self.notas:
            prom += pro

        prom = prom / len(self.notas)

        return prom

    def estado(self):
        resultado = self.promedio_notas()
        if resultado >= 13:
            return "Aprobado"
        elif resultado >= 11 and resultado <= 12:
            return "Subsa"    
        elif resultado >=0 and resultado <= 10:
            return "Jalado"

est1 = Estudiante("Pedro", "pedro@gmail.com")

est1.agregar_nota(11)
est1.agregar_nota(10)
est1.agregar_nota(4)
estad = est1.estado()
print(estad)





    

    

