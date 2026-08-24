#1. ingresa por teclado el monto a pagar y que imprima por consola
# el monto de propina que debo de dar siendo el 10%
monto_pagar = input('Ingresa tu monto: ')
propina = int(monto_pagar) * 0.1
print(f'El monto de la propina es: {propina}')
print("----")

#2. Dado un total de segundos (3746), Calcula cuantas horas, minutos y segundos representa
#usando los operadores aritmeticos // y %
total = 3746
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f'Horas: {horas}, minutos: {minutos}, segundos: {segundos}')
print("----")

#3. Ingresa un numero digame si es par o impar (use el operador aritmetico %)
numero = input('Ingrese el numero: ')
divisible = int(numero) % 2 
print(divisible)
print("----")

#4. Ingresa un monto por teclado y luego haga lo siguiente:
# aumente 250 luego retire 400 y luego genere un cobro de
# interes del 5% (multiplicar por 1.05)
monto = input('ingrese un monto: ')
aumentar = int(monto) + 250
retiro = aumentar - 400
cobro = retiro * 1.05
print(cobro)
