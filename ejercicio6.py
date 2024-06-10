'''Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''

def es_palindronomo(palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]
print(es_palindronomo("radar"))
print(es_palindronomo("python"))