class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def mostrar_info(self):
        print(f"{self.nombre} gana {self.sueldo}")

#Heredamos mi clase empleado para : 

class EmpleadoVentas(Empleado):
    pass

#Al heredar de una clase jalaremos toda su configuracion 
# (metodos y atributos publicos y protegidos)
vendedor = EmpleadoVentas("Roxana", 1200)

vendedor.mostrar_info()

#Clas padre / superclase = La clase original (Empleado)
#Clase hija / subclase = La clase que hereda (EmpleadoVentas)
#Herencia =  La hija obtiene automaticamente atributos y metodos del padre


class EmpleadoMkt(Empleado):
    def __init__(self, nombre, sueldo, comision):
        # Cuando queremos reutilizar el mismo metodo de la clase llamamos super()
        super().__init__(nombre, sueldo)
        self.comision = comision


############################

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiedo :p")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo zzz")

class Gato(Animal):
    #Si queremos sobre escribir metodo del padre usarmos super
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

    def araniar(self):
        print(f"{self.nombre} esta arañando")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

    def comer(self):
        super().comer()
        print(f"Esta comiendo feliz!")


g = Gato("Michi", 2)

p = Perro("Chiwi")

g.comer()
g.araniar()
p.dormir()
p.ladrar()
p.comer()



##########################
# Crear una clase padre llamada Figura y dos clases hijos llamada Cuadrado y Triangulo. La clase Figura tiene el atributo  nombre y un metodo area() que retorna 0 por defecto. La clase Cuadrado tiene un atributo adicional lado y la clase Triangulo tiene atributo base y altura, ambas clases heredan de Figura y se necesita sobreescribir el metodo area()

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        return 0

class Cuadrado(Figura):
    def __init__(self, nombre, lado):
        super().__init__(nombre)
        self.lado = lado

    def area(self):
        super().area()
        print(f"El área del cuadrado es: {self.lado * self.lado}")

class Triangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def area(self):
        super().area()
        print(f"El área del triángulo es: {(self.base * self.altura) / 2}")

c = Cuadrado("Cuadrado", 3)
c.area()

t = Triangulo("Triangulo", 3, 2)
t.area()

# Clase Persona y clase Guerrero y Mago en la cual Persona tiene nombre y vida 
# (valor predeterminado es 100) y un metodo recibir_danio(cantidad) que resta vida hasta llegar a 0. 
# Guerrero tiene el atributo fuerza y un metodo atacar() que imprime el daño causado segun la fuerza. 
# La clase Mago tiene atributo mana y un metodo lanza_hechizo() que solo funciona si tiene suficiente mana (sino muestra un mensaje de error)


class Persona:
    def __init__(self, nombre, vida = 100):
        self.nombre = nombre
        self.vida = vida

    def recibir_danio(self, cantidad):
        if cantidad > self.vida:
            self.vida = 0
            print("Ya te moriste")
        else:
            self.vida -= cantidad
            print("Daño recibido")

    
class Guerrero(Persona):
    def __init__(self, nombre, fuerza, vida=100):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atacar(self):
        print(f"El daño causado es: {self.fuerza}")

class Mago(Persona):
    def __init__(self, nombre, mana, vida=100):
        super().__init__(nombre, vida)
        self.mana = mana

    def lanza_hechizo(self, costo_mana):
        if costo_mana > self.mana:
            print("no tienes suficiente mana")
        else:
            self.mana -= costo_mana
            print("Hechizo lanzado")


print("------------")

persona = Persona("Anakin", 80)
persona.recibir_danio(110)
print(f"Vida de {persona.nombre}: {persona.vida}")

persa = Guerrero("Leonidas", 100)
persa.atacar()

merlin = Mago("Merlin", 50, 70)

merlin.recibir_danio(20)
print(f"Vida de {merlin.nombre}: {merlin.vida}")

merlin.lanza_hechizo(100)
merlin.lanza_hechizo(40)

print(f"Mana restante de {merlin.nombre}: {merlin.mana}")
            
