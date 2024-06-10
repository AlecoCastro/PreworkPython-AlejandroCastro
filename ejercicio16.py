'''Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

def contar_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = sum(1 for num in lista if num % 2 != 0)
    return pares, impares

lista = list(map(int, input("Ingresa los números de la lista separados por espacio: ").split()))
pares, impares = contar_pares_impares(lista)

print(f"La lista tiene {pares} números pares y {impares} números impares.")