'''Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''

def contar_palabras():
    oracion = input("Por favor, ingresa una oración: ")
    palabras = oracion.split()
    cantidad_de_palabras = len(palabras)
    print("La cantidad de palabras en la oración es: ", cantidad_de_palabras)

contar_palabras()