# 1. Crea una funcion calcular_igv en la cual pide el precio y retorne el precio final aplicado el igv (18%) - puede utilizar lambda

def calcular_igv():
    precio = int(input("Ingrese el precio: "))
    return(precio * 1.18)

# 2. Convierte la temperatura ingresada en la funcion cambiar_temperatura de Celcius a Farenheit - puede utilizar lambda

def cambiar_temperatura(temp:int):
    nueva_temp = 0
    nueva_temp = (temp * 9/5) + 32
    print(f"La nueva temperatura es: {nueva_temp} °F")


# 3. Dado un diccionario de un producto (nombre, precio, stock) utiliza if-elif-else para clasificar el stock en "Sin Stock" 
# (si el stock es 0), "Stock Bajo" (si el stock es entre 1 y 10) y "Disponible"(si el stock es mas que 10)

producto = {"nombre":"teclado", "precio": 100, "stock": 4}
def calsificar_producto():
    cant_stock = producto["stock"]

    if cant_stock == 0:
        print(f'El producto {producto["nombre"]} esta sin stock')
    elif cant_stock > 0 and cant_stock <=10:
        print(f'El producto {producto["nombre"]} tiene stock bajo')
    else:
        print(f'El producto {producto["nombre"]} esta disponible')

# 4. Usando un while, simula un cajero automatico simple que pida una clave hasta que el usuario la ingrese correctamente, 
# usando 3 intentos como maximo, sino indica que la cuenta fue bloqueada.

def cajero_automatico():
    clave_correcta = 1234
    cant = 1
    while(cant <=3):
        clave = int(input("Ingrese su clave de 4 digitos: "))
        if clave == clave_correcta:
            print("Bienvenido!")
            return
        else:
            print("Clave incorrecta!")
            cant += 1
    print("Intentos maximos! Su cuenta fue bloqueada")  
    
# 5. Crear una funcion calcular_area_circulo(radio) que retorne el area (3.1415 como valor de pi) - puede utilizar lambda
def calcular_area_circulo(radio):
    return round(3.1415 * radio**2, 2)


# 6. Crear una funcion procesar_notas(nombre, *notas) que calcule y retorne el promedio y 
# luego clasifique el resultado con if-elif-else en una segunda funcion clasificar(promedio)

def procesar_notas(nombre, *notas):
    promedio = 0
    for nota in notas:
        promedio += nota
    promedio = promedio / len(notas)

    return promedio

def clasificar(promedio):
    if promedio >= 12:
        return("Alumno Aprobado")
    else:
        return("Alumno Desaprobado")

# 7. En una lista de 5 elementos crear una funcion obtener_por_indice(lista, indice) 
# que capture el error IndexError si el indice no existe

lista_numeros = [1, 2, 3, 4, 5]

def obtener_por_indice(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "El indice no existe"

# BONUS!
# 8. Crear una funcion con while True que pida numeros al usuario y los sume manejando 
# un try-except en el que caso que se ingrese un texto en vez de numeros y que al escribir Salir, 
# termine la sumatoria sin lanzar el error

def sumando_numeros():
    
    sumas = 0
    condicion = ""

    while(True):

        try:
            condicion = input("Ingrese el numero o salir: ")

            if condicion.lower() == "salir":
                print(f"suma total: {sumas}")
                return
            else:
                sumas += int(condicion)   
                print(f"suma total: {sumas}")  
        except:
            print("No es valido! ")

print("Ejer1:")
precioFinal = calcular_igv()
print(f"El nuevo precio es: {precioFinal}")

print("Ejer2:")
cambiar_temperatura(20)

print("Ejer3:")
calsificar_producto()

print("Ejer4:")
cajero_automatico()

print("Ejer5:")
resultado = calcular_area_circulo(5)
print(resultado)

print("Ejer6:")
prom = procesar_notas("pedro", 5, 2, 9)
clasificado = clasificar(prom)
print(clasificado)

print("Ejer7:")
resultado = obtener_por_indice(lista_numeros, 10)
print(resultado)

print("Ejer8:")
sumando_numeros()
