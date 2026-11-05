# ====================================================================
# EJERCICIO 3
# ====================================================================
# a) Crea una clase llamada Libro que en su constructor (__init__) reciba: titulo, autor y paginas. Agrega un metodo llamado resumen() que imprima algo como:
#    "El libro TITULO fue escrito por AUTOR y tiene PAGINAS paginas"
#    Luego crea una instancia de la clase y llama al método
#    resumen().

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def resumen(self):
        print(f"El libro {self.titulo} fue escrito por {self.autor} y tiene {self.paginas} paginas")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro1.resumen()


# b) Crea una clase llamada CuentaBancaria con:
#    - Atributos: titular (publico) y saldo (debe ser un atributo
#      PRIVADO, es decir, con doble guion bajo).
#    - Un getter para saldo usando el decorador @property.
#    - Un metodo depositar(monto) que aumente el saldo solo si el
#      monto es mayor a 0 (si no, mostrar un mensaje de error).
#    - Un metodo retirar(monto) que reste el saldo solo si hay
#      saldo suficiente (si no, mostrar un mensaje de error).
#    Crea una instancia y prueba los métodos con al menos 2
#    depositos y 2 retiros (uno de ellos debe fallar a proposito
#    para comprobar la validacion).

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return(f"El monto {monto} fue depositado, Saldo actual {self.__saldo}")

        return(f"Error: No es posible depositar {monto}, El monto a depositar debe ser mayor a 0")

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            return(f"Monto retirado es {monto}, Saldo actual es: {self.__saldo}")

        return(f"Error: No es posible retirar {monto}, Su saldo actual es {self.__saldo}")

cuenta1 = CuentaBancaria("Kevin", 500)

print(cuenta1.depositar(100))
print(cuenta1.depositar(-20))
print(cuenta1.retirar(500))
print(cuenta1.retirar(200))