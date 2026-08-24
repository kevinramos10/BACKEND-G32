# String (Texto)
# Se identifican por comillas simples o comillas dobles
# Se puede crear string en varias lineas utilizando la triple comilla
#backslash para poder utilizar comillas dentro del texto
nombre = 'Eduardo O\'Conner'
#Con la letra r tambien deja imprimir backslash
ruta = r'C:\documentos\etc'

texto = '''Hola soy su profesor.
    El dia de hoy seguiremos utilizando python.
    Hoy se haran ejercicios'''

apellido = "Ramos"

#El prefijo f antes del string para poder escribir codigo python
saludo = f'Hola mucho gusto {apellido}'
print(saludo)

#Para el uso del format tambien sirve para codigo python
saludo2 = 'Hola {}, mucho gusto'.format(apellido)
print(saludo2)


#ENTEROS
edad = 30

#DECIMALES O FLOAT
estatura = 1.88

#BOOLEAN
aprobado = True
viudo = False

#Las variables nunca pueden empezar con: numeros, caracteres especiales
#No se recomiendas empezar con _ ya que eso usa en encapsulamiento

#SABER TIPO DE VARIABLE
print(type(estatura)) #Nos imprimi el tipo de la variable del caracter

