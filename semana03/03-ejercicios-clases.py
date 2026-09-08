# 1. Crear una clase Producto en el cual su constructor reciba el nombre, precio, stock. 
# Agregar un metodo esta_disponible en el cual muestre True si lo esta o no.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def esta_disponible(self):
        return self.stock > 0
    
producto1 = Producto("celular", 1000, 11)
print(producto1.esta_disponible())

# 2. Crear una clase CarritoCompras en la cual en el constructor reciba el cliente y que inicialice una lista vacia de productos. 
# Asi mismo, tener los metodos agregar_producto(nombre, precio), y cada producto se debe de guardar en un diccionario 
# {"nombre":nombre, "precio":precio} a la lista. Y otro metodo llamado calcular_total en el cual recorrera la lista de productos y 
# me dara el precio a pagar. Y un metodo llamado limpiar_carrito en el cual limpiara todos los productos de la lista

class CarritoCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio}) 

    def calcular_total(self):
        total = 0
        for p in self.productos:
            total += p["precio"]
        return total

    def limpiar_carrito(self):
        self.productos = []


carrito1 = CarritoCompras("Pedro")
carrito1.agregar_producto("mause", 10)
carrito1.agregar_producto("pc", 10)
carrito1.agregar_producto("dsa", 1)
print(carrito1.calcular_total())
carrito1.limpiar_carrito()
print(carrito1.calcular_total())

# 3. Crear una clase Sesion (simular el login y logout)  en la cual en el constructor recibamos un usuario y un atributo 
# que sea activa = False. Agregar el metodo iniciar_sesion que cambia activa = True y cerrar_sesion cambia activa = False y 
# un metodo verificar_acceso que imprima "Acceso Permitido" si activa = True o "Acceso Denegado" si activa = False

class Sesion:
    def __init__(self, usuario):
        self.usuario = usuario
        self.activa = False

    def iniciar_sesion(self):
        self.activa = True

    def cerrar_sesion(self):
        self.activa = False

    def verificar_acceso(self):
        if self.activa:
            print("Acceso Permitido!")
        else:
            print("Acceso Denegado!")

sesion1 = Sesion("Pedro")
sesion1.iniciar_sesion()
sesion1.verificar_acceso()
sesion1.cerrar_sesion()
sesion1.verificar_acceso()