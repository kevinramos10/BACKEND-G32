class Persona:
    nombre = ""
    edad = 0

#instancia: es crear una copia completa de toda la clase
#al momento de crear una instancia todos los atributos o metodos van a ser propios de esa variable
p1 = Persona()
p2 = Persona()
print(type(p1))

#Como se puede acceder a los atributos de la clase?
p1.nombre = "Eduardo"

p2.nombre = "Ana"

#al editar un atributo de la instacia solamente se va a modificar en esa instacia y no en las otra
print(p1.nombre)
print(p2.nombre)

#Si una clase al momento de crear unstacia quieor inicializar los atributos entonces debemos
#usar el constructor

class Gato:
    #Cuando creamos una funcion dentro de una clase esta pasa a llamarse metodo porque
    #solo va funcionar dentro de la clase

    #En python siempre el primer parametro de un metodo es self asi mismo, sirve para indeicar
    #que los cambios que hagamos se realicen a la misma instacia de la clase

    sexo = "Masculino"
    # En python no hay this se usa self:
    def __init__(self, nombre, raza, peso):
        #Para usar cualquier atributo o metodo de la misma clase usamos el "self"
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        # Las variables que yo cree dentro de __init__ estos seran creados como atributos
        #de la clase entonces podran ser usandos en todos sus metodos

g1 = Gato("muchi", "Persa", 2.5)
print(g1.nombre)
print(g1.sexo)


#Para ti que significa el self y que significa una clase
#Clase: Una plantilla que tenemos que podria usarse
#Self: Es un objeto que se usa para acceder a las caracteristicas