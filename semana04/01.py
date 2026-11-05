# ====================================================================
# EJERCICIO 1
# ====================================================================
# Crea un programa en Python que:
 
# a) Solicite por teclado el precio de un producto (usar input()) y lo convierta a numero decimal (float).
# b) Si el precio es mayor o igual a 50, aplique un descuento del 15%; si no, no aplique descuento.
# c) Imprima el precio final usando f-strings, con 2 decimales. Ejemplo de salida: "El precio final es: 42.50"

precio_producto = float(input("Ingrese el precio del producto: "))

if precio_producto >= 50:
    precio_producto *= 0.85

print(f"El precio final es: {precio_producto:.2f}")

# Adicionalmente, dada la siguiente lista de precios:
# precios = [12.5, 8.9, 25.0, 3.75, 40.2]
# d) Usando un bucle for, calcula e imprime la suma total y el promedio de los precios (el promedio con 2 decimales).

precios = [12.5, 8.9, 25.0, 3.75, 40.2]
suma_total = 0
for precio in precios:
    suma_total += precio

promedio = suma_total / len(precios)

print(f"La suma total de los precios es: {suma_total}")
print(f"El promedio de los precios es: {promedio:.2f}")