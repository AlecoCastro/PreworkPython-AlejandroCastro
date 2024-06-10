'''Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

def suma_pares_hasta_100():
    suma = 0
    for numero in range(2, 101, 2):
        suma += numero
    return suma

resultado = suma_pares_hasta_100()
print(f"La suma de todos los números pares del 1 al 100 es: {resultado}")