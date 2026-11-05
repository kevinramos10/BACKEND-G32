# ====================================================================
# EJERCICIO 2
# ====================================================================
# Dada la siguiente lista de diccionarios:
 
# productos = [
#     {"nombre": "Cuaderno", "precio": 4.5, "stock": 20},
#     {"nombre": "Lapicero", "precio": 1.2, "stock": 0},
#     {"nombre": "Mochila", "precio": 85.0, "stock": 5}
# ]
 
# a) Crea una funcion llamada mostrar_disponibilidad(productos) que recorra la lista con un for y, por cada producto, imprima:
#    - "PRODUCTO tiene stock disponible" si el stock es mayor a 0
#    - "PRODUCTO no tiene stock" si el stock es igual a 0
#    (reemplaza PRODUCTO por el nombre real de cada producto)

productos = [
    {"nombre": "Cuaderno", "precio": 4.5, "stock": 20},
    {"nombre": "Lapicero", "precio": 1.2, "stock": 0},
    {"nombre": "Mochila", "precio": 85.0, "stock": 5}
]

def mostrar_disponibilidad(productos):
    for producto in productos:
        if producto["stock"] > 0:
            print(f'{producto["nombre"]} tiene stock disponible')
        elif producto["stock"] == 0:
            print(f'{producto["nombre"]} no tiene stock')
            
mostrar_disponibilidad(productos)
 
# b) Crea una función llamada clasificar_nota(nota) que reciba una nota del 0 al 20 y retorne (usando if-elif-else):
#    - "Excelente" si la nota es entre 17 y 20
#    - "Bueno" si la nota es entre 14 y 16
#    - "Regular" si la nota es entre 11 y 13
#    - "Desaprobado" si la nota es menor a 11
#    Prueba la funcion con al menos 3 notas diferentes e imprime los
#    resultados.

def clasificar_nota(nota):
    if 17 <= nota <= 20:
        return("Excelente")
    elif 14 <= nota <= 16:
        return("Bueno")
    elif 11 <= nota <= 13:
        return("Regular")
    elif nota < 11:
        return("Desaprobado")
    else:
        return("Nota no valida")

print(clasificar_nota(20))
print(clasificar_nota(14))
print(clasificar_nota(12))