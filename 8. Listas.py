#Ejercicios

#E1  CRUD de pasajero con clases Pasajero + list
#Sistema completo: agregar, listar, buscar por cédula, modificar y eliminar pasajeros. Usa clase Pasajero y una list como contenedor.
#Entrada: opción del menú y datos
#Proceso operaciones sobre la lista con validaciones
#Salida: resultado de cada acción

class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)


# --- Programa principal ---
lista = []
menu=["1. Agregar", "2. Listar", "3. Buscar", "4. Modificar" ,"5. Eliminar", "6. Ordenar por nombre", "0. Salir"]
while True:
    print("Menú gestión de Pasajeros")
    print("============================================")  
    for opcion in menu:
      print(opcion)
    op = input("Inserte una opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        if not lista:
            print("No hay pasajeros para ordenar")
        else:
            lista.sort(key=lambda p: p.nombre)
            print("Lista ordenada por nombre ✓")

    else:
      print("Vuelva pronto!")
     




#E2 Estadisticas de una lista de notas
#Dada una lista de N notas, calcular: promedio, máxima, mínima, cantidad de aprobados y el nombre del mejor estudiante (paralelo con nombres).
#Entrada: N, lista de nombres y lista de notas
#Proceso recorridos en paralelo para calcular estadísticas
#Salida: todas las métricas

import math

nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas   = [ 8,     6,      10,      7,      5]

# Python trae todo esto:
prom = sum(notas) / len(notas)
desv_estandar = math.sqrt(sum((n - prom) ** 2 for n in notas) / len(notas))

print(f"Promedio: {prom:.2f}")
print(f"Desviación estándar: {desv_estandar:.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

prom_manual = suma / len(notas)

# Segundo bucle para acumular las diferencias al cuadrado respecto al promedio
suma_cuadrados = 0
for n in notas:
    suma_cuadrados += (n - prom_manual) ** 2

desv_manual = math.sqrt(suma_cuadrados / len(notas))

print(f"\nManual → prom: {prom_manual:.2f}, desv: {desv_manual:.2f}, máx: {maxima}, aprob: {aprob_manual}")

#E3 Ordenar una lista
#Implementar el algoritmo de ordenamiento burbuja sobre una lista. Luego comparar con list.sort().
#Entrada: una lista de números desordenada
#Proceso: recorrer varias veces intercambiando pares consecutivos
#Salida: la lista ordenada

def bubble_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for vuelta in range(n - 1):
        # Bandera para optimizar: si en una vuelta no hubo swaps, ya está ordenado
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if arr[i] > arr[i + 1]:
                # Intercambio en una línea
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hubo_swap = True
        if not hubo_swap:
            break
    return arr


# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión
ordenada = bubble_sort(notas)
print(ordenada)                            # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]                           # copia para no romper el original
copia.sort()
print(copia)                               # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)                               # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)                            # ['a', 'el', 'python', 'código']





#E3 Adicional Ordenar una lista
#Implementar el algoritmo de ordenamiento burbuja sobre una lista. Luego comparar con list.sort().
#Entrada: una lista de números desordenada
#Proceso: recorrer varias veces intercambiando pares consecutivos
#Salida: la lista ordenada

def selection_sort(lista):
    n = len(lista)
    arr = lista[:]  # Copia para no modificar el original
    
    for i in range(n - 1):
        # Asumimos que el primer elemento no ordenado es el mínimo
        idx_min = i
        
        # Buscamos el verdadero mínimo en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j
                
        # Si encontramos un valor menor, lo colocamos al inicio de la parte no ordenada
        if idx_min != i:
            arr[i], arr[idx_min] = arr[idx_min], arr[i]
            
    return arr


# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

ordenada_bubble = bubble_sort(notas)
ordenada_selection = selection_sort(notas)

print("Original: ", notas)               # [5, 2, 8, 1, 9, 3, 7]
print("Selection:", ordenada_selection)  # [1, 2, 3, 5, 7, 8, 9]



#Propuestos 
#P1 Contar apariciones de un valor
#Dada una lista de números y un valor, contar cuántas veces aparece.
#Entrada: lista=[1,3,2,3,4,3], v=3
#Salida: 3 aparece 3 veces

lista = [1, 3, 2, 3, 4, 3, 5]
v = 5

# Manual
print("Manual")
count = 0
for x in lista:
    if x == v:
        count += 1
print(f"{v} aparece {count} veces")
print("====================")
print("Python")
# Pythonic
print(f"{v} aparece {lista.count(v)} veces")



#P2 invertir una lista
#Invertir el orden de una lista sin usar lista.reverse().
#Entrada: [1, 2, 3, 4, 5]
#Salida: [5, 4, 3, 2, 1]

lista = [1, 2, 3, 4, 5]

# Con bucle
print("Con bucle")
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)
print("=================")
print("Con Slicing")
# Con slicing (pythonic)
print(lista[::-1])
print("=================")
print("Con Reversed")
# Con reversed
print(list(reversed(lista)))

 #P3 Numeros unicos
#Dada una lista con posibles duplicados, retornar una lista sin duplicados manteniendo el orden.
#Entrada: [1, 3, 2, 3, 4, 1]
#Salida: [1, 3, 2, 4]

nums = [1, 3, 2, 3, 4, 1, 5, 2]

# Manual (mantiene orden)
unicos = []
for x in nums:
    if x not in unicos:
        unicos.append(x)
print(unicos)                       # [1, 3, 2, 4, 5]

# Rápido (NO mantiene orden)
print(list(set(nums)))

# Rápido MANTENIENDO orden (Python 3.7+)
print(list(dict.fromkeys(nums)))    # [1, 3, 2, 4, 5]



#P4 Segundo mayor
#Encontrar el segundo número más grande de una lista (sin ordenar toda la lista).
#Entrada: [5, 2, 9, 7, 9, 3]
#Salida: Segundo mayor: 7

nums = [5, 2, 9, 7, 9, 3, 8]

# Dos campeones: mayor y segundo
mayor = float("-inf")
segundo = float("-inf")

for n in nums:
    if n > mayor:
        segundo = mayor         # el que era mayor pasa a segundo
        mayor = n
    elif n > segundo and n < mayor:
        segundo = n

print(f"Mayor: {mayor}")
print(f"Segundo: {segundo}")





#P5 Fusionar dos listas ordenadas
#Dadas dos listas ordenadas, fusionarlas en una tercera también ordenada, sin usar sort().
#Entrada: a=[1,3,5], b=[2,4,6,8]
#Salida: [1, 2, 3, 4, 5, 6, 8]

a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

resultado = []
i = j = 0

# Recorremos las dos listas a la par
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        resultado.append(a[i])
        i += 1
    else:
        resultado.append(b[j])
        j += 1

# Añadimos lo que quede de la más larga
resultado.extend(a[i:])
resultado.extend(b[j:])
print("Ordenado:")
print(resultado)                    # [1, 2, 3, 4, 5, 6, 7, 8, 10]

