'''Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''



peso = float(input("Por favor, introduce tu peso: "))
altura = float(input("Por favor, introduce tu altura: "))

IMC = (peso / (altura * altura))

print("Tu masa corporal es:", IMC)