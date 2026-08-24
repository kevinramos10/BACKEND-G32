# Coleccion de datos Editable pero no es ordenada
# Se suelen utilizar para almacenar inforamcion y luego corroboara su contenido sin importar algun orden en especifico
roles = {"USUARIO", "ADMIN", "INVITADO", "ALUMNO", "PROFESOR"}
print(roles) #No es ordenada imprime al azar 

# Para poder agreagar nuevos datos
roles.add("SUPERADMIN")
print(roles)

# Para eliminar un dato que esta en la coleccion
roles.remove("SUPERADMIN")
print(roles)

#Para poder saber si hay algun dato que quier
print("COORDINADOR" in roles)
print("COORDINADOR" not in roles)