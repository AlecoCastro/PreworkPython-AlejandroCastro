'''Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''

def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

minutos = int(input("Ingresa el número de minutos: "))
horas, minutos_restantes = convertir_minutos(minutos)

print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
