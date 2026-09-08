# 1. Crear un sistema para calcular sueldos de distintos tipos de empleados
# Clase base Empleado
# atributos: nombre (publico) y sueldo_base (privado)
# crear su getter y setter para el sueldo_base (el setter no debe permitir valores negativos)
# metodo calcular_sueldo() que retorna el sueldo_base
# mostrar_info() imprime el nombre y el sueldo calculado

# Clase hijas
# EmpleadoVentas y su atributo comision (monto fijo) y sobreescribir calcular_sueldo() para que retorne el sueldo_base + comision
# EmpleadoTiempoParcial y sus atributos horas_trabajadas y pago_por_hora y sobreescribir calcular_sueldo() para que retorne el horas_trabajas * pago_por_hora e ignora el sueldo base

# Para validar: 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Calcular e imprimir el total de la planilla (suma de todos los sueldos de los empleados)



class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo < 0:
            return("No puede ser negativo")
        else:
            self.__sueldo_base = nuevo_sueldo

    def calcular_sueldo(self):
        return self.__sueldo_base

    def mostrar_info(self):
        print(f'La persona {self.nombre} su sueldo es: {self.calcular_sueldo()}')

class EmpleadoVentas(Empleado):
    def __init__(self, nombre, sueldo_base, comision = 10):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision

    
class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.pago_por_hora

empleados = [
    Empleado("Ana", 1500),
    EmpleadoVentas("Carlos", 1200, comision=300),
    EmpleadoTiempoParcial("Lucía", 0, horas_trabajadas=80, pago_por_hora=15),
]

for empleado in empleados:
    empleado.mostrar_info()

total_planilla = sum(empleado.calcular_sueldo() for empleado in empleados)
print(f'\nTotal de la planilla: {total_planilla}')


# --------------------------------------

# 2. Crear un sistema de inventario simple
# Clase base Producto
# atributos: nombre, precio(privado) y stock
# crear getter y setter para el precio (no negativos)
# metodo calcular_precio_final() que por defecto retorna el precio sin cambios
# metodo vender(cantidad) que resta del stock si hay suficiente, sino, muestra un mensaje de error y no resta stock

# Clases hijas
# ProductoConDescuento: atributo porcentaje_descuento. sobreescribir calcular_precio_final() aplicar el dscto sobre el precio
# ProductoImportado: atributo impuesto_aduanero (porcentaje). sobreescribir calcular_precio_final() para sumar ese impuesto al precio

# Para validar 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Intentar asignar un precio negativo a alguno de ellos usando el setter y comprobar el mensaje de error



class Producto:
    def __init__(self, nombre, stock):
        self.nombre - -nombre
        

