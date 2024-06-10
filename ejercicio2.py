'''Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''


precio_total = float(input("introduzca monto total: "))
precio_descuento = precio_total * 1.15
print("El monto con propina es: ", precio_descuento)