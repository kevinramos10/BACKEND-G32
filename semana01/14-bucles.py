# For plano (sin el uso de ninguna coleccion de datos)
# range(x,y,z)
# Si solo utilizamos un parametro va ser el tope
# x > tope, es decir hasta que numero va incrementar
# y > Inicio, es decir desde que numero va empezar osea del (5,10) 5 al 10
# z > Modificador, es decir de cuanto en cuanto se va incrementar o decrementar (5,10,2)

for numero in range(10):
    print(numero)
print("--")
for numero in range(5, 10):
    print(numero)
print("--")
for numero in range(5, 10, 2):
    print(numero)

# Los for son mas utiles dentro de las colecciones de datos porque puedo iterar
# y nabegar por cada uno de sus elementos

numeros = [10, 15, 7, 20, 13, 9]
print("---")
for x in numeros:
    print(x)
