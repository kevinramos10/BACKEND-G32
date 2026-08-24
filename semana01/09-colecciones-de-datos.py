# Listas (Arreglos)
#Coleccion de datos ordenada y editable

frutas = ['manzana', 'pera', 'kiwi', 'platano', 1, True, 10.5]

#ordenada (la posicion empiza desde 0)
print(frutas[0])

#se puede recorrer las litas de izq a der como viceversa
print(frutas[-1])

#puedo sacar una sub-lista
print(frutas[1:3]) #Nueva lista desde la 1 hasta una antes de la 3

#Si no se le pone posicion inicial agarra del inicio
print(frutas[:3])

#Si no se le pone posicion al final agarra desde la inicio hasta el final
print(frutas[3:])


# agregamos nuevos elementos al final de la lista
frutas.append('sandia')

#insertar elemento en la posicion indicada
frutas.insert(1, 'mango')
print(frutas)

#remove elimina el valor si lo encuentra y si no hay lanza error
frutas.remove(1)

#pop elimina el contenido por si indice y devuelve el valor eliminado
eliminado = frutas.pop(5)
print(eliminado)
print(frutas) #Ya no se ve el True en la lista de frutas

#ordena alfabeticamente los elementos de la lista, solo funciona en caso que todos sean string
frutas.sort()
print(frutas)

#Reverse invierte el orden actual el ultimo al primero y asi sucesivamente...
frutas.reverse()

#len devulve la cantidad de elementos que hay en la lista
longitud = len(frutas)
print(longitud)

#Clear limpia toda la lista y la deja vacia
frutas.clear()