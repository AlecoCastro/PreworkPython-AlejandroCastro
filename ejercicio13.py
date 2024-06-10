'''Escribe un programa que determine si un número ingresado por el usuario es primo o no.'''

def es_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Ingresa un número: "))
if es_primo(num):
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")