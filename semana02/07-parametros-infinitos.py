#en el caso recibimos una cantidad indeterminada de parametros usamos *args (arguments)
def promedio_notas(*notas):    
    sum_promedio = 0
    promedio = 0
    cont = 0
    for n in notas:
        sum_promedio += n
        cont += 1

    promedio = sum_promedio / cont
    
    print(promedio)

#Al pasarle los parametros seran con , 
promedio_notas(20, 20, 20)

# Se puede tambien combinar los parametros con los *args
# No se puede colocar otro parametro luego de los *args
# Para el tipado de una coleccion de datos si queremos indicar que todos los elementos van a ser int, entonces [int,...]
# si queremos indicar que la tupla va a tener SOLO 2 ELEMENTOS y esos van a ser int y str, entonces [int, str]
# tuple > tupla 
# dict > diccionario
# list > lista
# object > conjunto
print("----------")

def promedio_notas_alumno(nombre:str, *notas: int):
    print(nombre)
    print(notas)

promedio_notas_alumno("Eduardo", 10, 20, 30, 50)