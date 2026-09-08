# Python tenemos al posibilidad de crear funciones en 1 sola inea y esta sse conocen como 
#funciones lambda

sumar = lambda num1, num2: num1 + num2 if num1 > 10 else num1*num2

resultado = sumar(5,10)
print(resultado)


#Necesito una funcion es_correo que verifique qie el correo contiene un @ y un . usando 
#lambda funcions y ademas dentro de los str se puede usar la palabra in para ver si 
#esta o no esta ese caracter

es_correo = lambda correo: "@" and "." in correo 


#Necesito una funcion generar_slug
#slug es convertir el texto "Bienvenidos a la clase" a "bienvenidos-a-la-clase", es
#decir, convertir los espacion por signos y lo pone todod en minuscila
#puede ysar la funcion .lower() y la funcion .replace()

generar_slug = lambda frase: print(frase.lower().replace(" ", "-"))

resultado = es_correo("kevin@dads.com")
print(resultado)

print("-----")

generar_slug("Bienvenidos a la clase")