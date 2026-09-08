class CuentaBancaria:
    def __init__(self, titular, saldo, cuenta):
        self.titular = titular
        self.saldo = saldo
        #Cuando se crea un atributo con un subguion es protegido 
        # se puede acceder fuera de la clase pero no es buena 
        # practica deber accerder cosa que no pasa en otros lenguajes de programacion
        self._cuenta = cuenta
        self.__entidad_financiera = "BCP"


cuenta1 = CuentaBancaria("Eduardo", 500, 1525-4515156-1545)
print(cuenta1.saldo)
#Se puede modificar los atriburos publicos

cuenta1.saldo = 2500
print(cuenta1.saldo)
print(cuenta1._cuenta)
#print(cuenta1.__entidad_financiera) Esto da error de no existe ya que no nos permite acceder fuera de la clase


class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__apellido = "Xi"

    #luego del decorador siempre se llama a un metodo, 
    # porque el decorador modifica la funcion adyacente con 
    # la propiedad del decorador, en este caso el decorador 
    # property sirve para definir la devoluacion del atributo 
    # privado

    @property
    def  nombre(self):
        return self.__nombre

    #Asi mismo se puede utilizar los metods para modificar y 
    # eliminar le contenido del atributo privado
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido

p1 = Persona("Eduardo")
print(p1.nombre)
p1.nombre = "Renato"
print(p1.nombre)
print(p1.apellido)


#Crear una clase llamda usuario, correo, apellido y password 
# el password debe ser privado y solo en el contructor inicializar 
# el nombre y correo cuando se quiera modificar el password usar 
# el property y no permitir el ingreso de un string que tenga 
# espacios o sea menor que 8 caracteres y asi mismo cuando se 
# quiera obtener el password devolver *****

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.__password = None

    @property
    def password(self):
        return "*********" if self.__password else "Ingrese una password"

    @password.setter
    def password(self, nuevo_password):
        if " " in nuevo_password or len(nuevo_password) < 8:
            print("El password no puede tener espacios ni ser menor de 8 caracteres")
        else:
            self.__password = nuevo_password


Usu1 = Usuario("Pedro", "Pedro123@gmail.com")

Usu1.password = "12345678"

print(Usu1.password)



class Empleado:
    def __init__(self, nombre, sueldo_base, horas_extras):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base
        self.__horas_extras = horas_extras


    def __calcular_pago_extra(self):
        valor_hora_extra = 20
        return self.__horas_extras * valor_hora_extra

    def calcular_sueldo_total(self):
        monto_extra = self.__calcular_pago_extra()
        return self.__sueldo_base + monto_extra

    def mostrar_boleta(self):
        print(f"""Empleado: {self.nombre}
        Sueldo base: {self.__sueldo_base}
        Pago extra: {self.__calcular_pago_extra()}
        Total: {self.calcular_sueldo_total()}""")


emp1 = Empleado("Juanito", 2000, 15)
emp1.mostrar_boleta()


class Caja:
    def __init__(self):
        self.__total = 0

    def __validar_monto(self, monto):
        if monto > 0:
            return True
        else:
            return False

    def agregar_venta(self, monto):
        valido = self.__validar_monto(monto)

        if valido:
            self.__total += monto
            return "Monto agregado"
        else:
            return "Monto no es valido"

    def mostrar_total(self):
        print(self.__total)

caja1 = Caja()

print(caja1.agregar_venta(100))
print(caja1.agregar_venta(50))
print(caja1.agregar_venta(-20))

caja1.mostrar_total()
