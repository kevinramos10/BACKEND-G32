secreto = 5

while(True):
    numero = int(input("Ingrese un numero: "))
    if numero == secreto:
        print("Ganaste!")
        break
    else:
        print("No es el numero, siga intentando...")


lista_precios = []
cont = 0
while(cont < 5):
    precio = int(input("Ingrese su precio: "))
    if precio <= 0 :
        continue
    else:
        lista_precios.append(precio)
        cont+=1       
    
print(lista_precios)