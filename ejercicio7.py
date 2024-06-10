'''Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.'''

def operacion_aritmetica():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    eleccion = int(input("Elige una operación (1-4): "))

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if eleccion == 1:
        resultado = num1 + num2
        print("La suma es: ", resultado)
    elif eleccion == 2:
        resultado = num1 - num2
        print("La resta es: ", resultado)
    elif eleccion == 3:
        resultado = num1 * num2
        print("La multiplicación es: ", resultado)
    elif eleccion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print("La división es: ", resultado)
        else:
            print("Error: División por cero no está permitida.")
    else:
        print("Elección inválida. Por favor, elige una operación del 1 al 4.")

operacion_aritmetica()