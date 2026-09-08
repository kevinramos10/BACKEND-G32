try: #intentalo
    numero = int(input("Ingresa un numero:"))
    print(10 / numero)
except ValueError: #excepcion (Si lo que intento no sale bien)
    print("Numero invalido")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
# y luego si por algun motivo se fenera un error no registrado
except:
    print("Error desconocido!")

print("Yo aun sigo trabajando")

# Tambien se puede filtrar los errores segun su tipo
