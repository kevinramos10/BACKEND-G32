#Pedir un numero por teclado, convertir ese numero a int y ser si el numero 
#es positivo solo si es mayor que 0

numero = input("Ingrese el número: ")

if int(numero) > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

#Se necesita registrar la venta por teclado y si la venta es mayor o igual a 100 soles
#entonces agregar un descuento del 10%, caso contrario no agregar descuento luego mostrar
#cuando se debe pagar
venta = int(input("Ingrese la venta: ")) 
pagar = 0
if venta >= 100:
    pagar = ve * 0.9
    print(f"Aplica el descuento del 10%, Pagar: {pagar} soles")
else:
    print(f"No tiene descuento, Pagar: {venta} soles")

#OPERADOR TERNARIO
#se usa si en el if-else solo vamos a tener una sola linea de codigo
monto_pagar = venta * 0.9 if venta >= 100 else venta
print(f"El monto a pagar es: {monto_pagar}")

#Usando el operador ternario indiqueme si el numero es par o impar
numero = 10
queEs = "par" if numero % 2 == 0 else "Impar"
print(queEs)



#IF ANIDADOS

nota = 60
if nota >= 90 and nota <= 100:
    print("Es excelente")
elif nota >=70 and nota < 90:
    print("Es bueno")
elif nota >=50 and nota < 70:
    print("Es regular")
else:
    print("Es malo")


#PARA CUANDO HACEN VARIAS CONDICIONALES
#SWITCH CASE en python no existe

#En base al numero del dia de la semana si es 1 es lunesa si es 2 martes y asi...
numero = 1
dia = ""
if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miercoles"
#...

#caluladora simple retorna el resultado
operador = ""
resultado = 0
numero1 = int(input("Ingrese un numero1: "))
numero2 = int(input("Ingrese un numero2: "))
operador = input("Ingrese el operador: ")

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2
else:
    print("Ese valor no es valido")

print(f"El resultado es: {resultado}")



