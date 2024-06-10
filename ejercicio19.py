'''Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no'''

año_actual = int(input("Introduzca el año a investigar: "))

año_bisiesto = año_actual / 4
comprobación = (año_actual / 100) / 4

if año_bisiesto == int(año_bisiesto):
  print("El año introducido es bisiesto")
elif comprobación == float(comprobación):
  print("El año introducido no es bisiesto")
