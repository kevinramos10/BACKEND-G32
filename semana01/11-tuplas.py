#Coleccion de datos que es ordenada pero no es editable
#Una vez que se crea ya no se puede modificar

persona = ("Eduardo", 30, "Arequipa")

print(persona[0])

#Desempaquetar los datos en variables independientes
nombre, edad, ciudad = persona

nombre = 'Ramoncito'
print(persona)


#CUIDADO AL CREAR TUPLAS DE UN SOLO ELEMENTO
numero = (1)
# Cuando yo agrego una tupla de un solo elemento y este no tiene una coma l
#final los parentesis que representan a la tupla no son considerados y al ginal 
#se eliminan
print(type(numero))

#Para crear elementos de tupla de un solo elemento se le coloca una coma al ginal
numero =(1,)
print(type(numero))