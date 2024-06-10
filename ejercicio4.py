'''Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

def contar_vocales():
    palabra = input("Por favor, ingresa una palabra: ")
    vocales = 'aeiouAEIOU'
    num_vocales = 0

    for letra in palabra:
        if letra in vocales:
            num_vocales += 1

    print("El número de vocales en la palabra es: ", num_vocales)

contar_vocales()
