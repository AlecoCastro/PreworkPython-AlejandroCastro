'''Crea un programa que sume todos los números en una lista ingresada por el
usuario.'''


def sumar_lista(lista):
    return sum(lista)

lista = list(map(int, input("Ingresa los números de la lista separados por espacio: ").split()))
suma = sumar_lista(lista)

print(f"La suma de los números en la lista es {suma}.")