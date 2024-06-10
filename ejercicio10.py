'''Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''


Numero = int(input("Introduza número de día: "))

if Numero > 7:
  print("ERROR")
if Numero < 0:
  print("ERROR")

if Numero == 1:
  print("El día es lunes")
if Numero == 2:
  print("El día es martes")
if Numero == 3:
  print("El día es miercoles")
if Numero == 4:
  print("El día es jueves")
if Numero == 5:
  print("El día es viernes")
if Numero == 6:
  print("El día es sabado")
if Numero == 7:
  print("El día es domingo")



