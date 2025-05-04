# Ejercicio 1. Función contar_caracteres : Descripción del ejercicio:
# Descripción: Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)
texto = "Análisis de datos"
numero_de_caracteres = contar_caracteres(texto)
print(f"El número de caracteres en la cadena es: {numero_de_caracteres}")

# Ejercicio 2. Función calcular_promedio : Descripción del ejercicio:
# Descripción: Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)
numeros = [2, 4, 7, 8, 9, 11, 14, 16, 19]
promedio = calcular_promedio(numeros)
print(f"El promedio de la lista es: {promedio}")

# Ejercicio 3. Función encontrar_duplicado : Descripción del ejercicio:
# Descripción: Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def encontrar_duplicado(lista):
    elementos_lista = set()
    for elemento in lista:
        if elemento in elementos_lista:
            return elemento
        elementos_lista.add(elemento)
    return None
numeros = [2, 4, 7, 7, 8, 9, 11, 11, 14, 16, 16, 19]  
duplicado = encontrar_duplicado(numeros)
print(f"El primer elemento duplicado es: {duplicado}")

# Ejercicio 4. Función enmascarado_datos : Descripción del ejercicio:
# Descripción: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarado_datos(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    return "#" * (len(cadena) - 4) + cadena[-4:]
variable = "Alejandro"
enmascarada = enmascarado_datos(variable)
print(f"Variable enmascarada: {enmascarada}")

# Ejercicio 5. Función es_anagrama : Descripción del ejercicio:
# Descripción: Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def es_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    return sorted(palabra1) == sorted(palabra2)
  
palabra1 = "Alejandro"  
palabra2 = "Ardejalon"
anagrama = es_anagramas(palabra1, palabra2)
print(f"¿Son anagramas? {anagrama}")

# Ejercicio 6. Función buscar_nombre : Descripción del ejercicio: Descripción: Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción. Caso de uso: Incorpora los siguientes nombres a la lista y comprueba que la función funciona correctamente: "Jaime", "Silvia" y "Ana".

def buscar_nombre():
    try:
        nombres_ingresados = input("Ingresa una lista de nombres separados por comas: ").split(",")
        nombres_ingresados = [nombre.strip() for nombre in nombres_ingresados]

        nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ").strip()

        if nombre_a_buscar in nombres_ingresados:
            print(f"¡El nombre '{nombre_a_buscar}' fue encontrado en la lista!")
        else:
            raise Exception(f"El nombre '{nombre_a_buscar}' no está en la lista.")
    except Exception as e:
        print(e)

buscar_nombre()

# Ejercicio 7. Función fibonacci : Descripción del ejercicio: Descripción: Crea una función que calcule el término n de la serie de Fibonacci utilizando recursión. Definición de la secuencia de Fibonacci: La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos números anteriores, comenzando con 0 y 1. La posición 0 es la primera: Ejemplo para los primeros 5 términos de la función de Fibonacci: [0, 1, 1, 2, 3] Primer término: 0 (0) Segundo término: 1 (1) Tercer término: 1 (0 + 1) Cuarto término: 2 (1 + 1) Quinto término: 3 (1 + 2)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(5):
    print(f"Término {i + 1}: {fibonacci(i)}")

''' Ejercicio 8. Función encontrar_puesto_empleado : Descripción del ejercicio: Descripción:
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si
está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí. Caso de uso:
empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
{'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
{'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}] '''

empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]
empleados_dict = {
    f"{empleado['nombre']} {empleado['apellido']}": empleado['puesto']
    for empleado in empleados
}
nombre_completo = "Iñaki Urrutia"
if nombre_completo in empleados_dict:
    print(f"El puesto de {nombre_completo} es: {empleados_dict[nombre_completo]}")
else:
    print(f"{nombre_completo} no trabaja aquí.")


# Ejercicio 9. Función cubo_numero usando lambdas: Descripción del ejercicio: Descripción: Crea una función en Python que calcule el cubo de un número dado mediante una función lambda

cubo_numero = lambda x: x ** 3
numero = 3
print(f"El cubo de {numero} es: {cubo_numero(numero)}")

# Ejercicio 10. Función resto_division usando lambdas: Descripción del ejercicio: Descripción: Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda a, b: "La división no se puede efectuar" if b == 0 else a % b
numero1 = 10
numero2 = 3
print(f"El resto calculado de dividir {numero1} entre {numero2} es: {resto_division(numero1, numero2)}")

# Ejercicio 11. Función numeros_pares usando lambdas y filter : Crea una función lambda que filtre los números pares de una lista dada.
# Caso de uso: lista_numeros = [24, 56, 2.3, 19, -1, 0]

lista_numeros = [24, 56, 2.3, 19, -1, -2, 0]
numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
print(f"Números pares: {numeros_pares}")

# Ejercicio 12. Función numeros_suma usando lambdas y map : Crea una función lambda que sume 3 a cada número de una lista dada.
# Caso de uso: lista_numeros = [24, 56, 2.3, 19, -1, 0]

lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_suma = list(map(lambda x: x + 3, lista_numeros))

print(f"Lista original: {lista_numeros}")
print(f"Resultado después de sumar 3: {numeros_suma}")

# Ejercicio 13. Función sumar_listas usando lambdas: Crea una función lambda que sume elementos correspondientes de dos listas dadas. Caso de uso: lista_numeros_1 = [1, 4, 5, 6 , 7 , 7] ; lista_numeros_2 = [3, 11, 34, 56]

sumar_listas = lambda lista1, lista2: list(map(lambda x: x[0] + x[1], zip(lista1, lista2)))
lista_numeros_1 = [1, 4, 5, 6, 7, 7] 
lista_numeros_2 = [3, 11, 34, 56]
resultado = sumar_listas(lista_numeros_1, lista_numeros_2)
print(f"Lista resultante al sumar elementos correspondientes: {resultado}")

'''Ejercicio 14. No te vayas por las ramas :
Explicación del ejercicio:
Descripción:
Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco
en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de
longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la
longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición
específica.
6. Implementar el método info_arbol para devolver información sobre la
longitud del tronco, el número de ramas y las longitudes de las mismas.

Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol  '''


class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "cantidad_ramas": len(self.ramas),
            "longitud_ramas": self.ramas
        }

# Casos de uso:
if __name__ == "__main__":
    
    # 1. Crear un árbol.
    mi_arbol = Arbol()
    print("Se ha creado un nuevo árbol.")

    # 2. Hacer crecer el tronco del árbol una unidad.
    mi_arbol.crecer_tronco()

    # 3. Añadir una nueva rama al árbol.
    mi_arbol.nueva_rama()

    # 4. Hacer crecer todas las ramas del árbol una unidad.
    mi_arbol.crecer_ramas()

    # 5. Añadir dos nuevas ramas al árbol.
    mi_arbol.nueva_rama()
    mi_arbol.nueva_rama()

    # 6. Retirar la rama situada en la posición 2.
    mi_arbol.quitar_rama(2)

    # 7. Obtener información sobre el árbol
    info = mi_arbol.info_arbol()
    print(info)
    
'''Ejercicio 15. Clase UsuarioBanco :

Explicación del ejercicio:
Descripción: Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

Código a seguir: 
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse. 
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario. 

Caso de uso: 

1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. 
2. Agregar 20 unidades de saldo de "Alicia". 
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia". 
4. Retirar 50 unidades de saldo a "Alicia".'''


class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente para retirar {cantidad} unidades.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad} unidades. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir {cantidad} unidades.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} ha transferido {cantidad} unidades a {self.nombre}. Saldo actual de {self.nombre}: {self.saldo}")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad} unidades. Saldo actual: {self.saldo}")

# Casos de uso

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# Agregar dinero a Alicia

alicia.agregar_dinero(20)

# Transferir dinero de Bob a Alicia

try:
    alicia.transferir_dinero(bob, 80)
except ValueError as e:
    print(e)

# Retirar dinero de Alicia

try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print(e)

'''Ejercicio 16. Función procesar_texto :

Explicación del ejercicio:
Descripción:
Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
contar_palabras, reemplazar_palabras, eliminar_palabra. Estas opciones son otras
funciones que tenemos que definir primero y llamar dentro de la función
procesar_texto.

Código a seguir:

1. Crear una función contar_palabras para contar el número de veces que
aparece cada palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original
del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo
de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto.
Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre
"contar", "reemplazar", "eliminar") y un número de argumentos variable
según la opción indicada.

Caso de uso:

texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
Dado el texto de ejemplo, llama a la función procesar_texto para probar sus
funcionalidades:

- Cuenta el número de veces que aparece cada palabra.
- Reemplaza la palabra texto por relato.
- Elimina la palabra ejemplo.'''

import re
from collections import Counter

def contar_palabras(texto):
    """Cuenta la cantidad de veces que aparece cada palabra en el texto."""
    palabras = re.findall(r'\b\w+\b', texto.lower())
    return dict(Counter(palabras))

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza una palabra específica en el texto."""
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    """Elimina una palabra específica del texto."""
    return re.sub(rf'\b{palabra}\b', '', texto).replace('  ', ' ')

def procesar_texto(texto, opcion, *args):
    """Procesa el texto según la opción indicada: 'contar', 'reemplazar' o 'eliminar'."""
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para reemplazar, proporciona la palabra original y la nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para eliminar, proporciona la palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción inválida. Usa 'contar', 'reemplazar' o 'eliminar'.")

# Casos de uso
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."

# Cuenta el número de veces que aparece cada palabra
print(procesar_texto(texto, "contar"))

# Reemplaza la palabra "texto" por "relato"
print(procesar_texto(texto, "reemplazar", "texto", "relato"))

# Elimina la palabra "ejemplo"
print(procesar_texto(texto, "eliminar", "ejemplo"))
