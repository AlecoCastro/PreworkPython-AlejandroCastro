'''Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''


def convertir_celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32
  

temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))

temperatura_fahrenheit = convertir_celsius_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit} grados Fahrenheit.")
