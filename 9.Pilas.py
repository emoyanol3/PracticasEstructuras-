#E1
#Inverrtir una cadena con pila
#Usar una pila para invertir una cadena de texto.
#Entrada: una cadena
#Proceso: empujar cada letra a la pila, luego desapilar hasta vaciarla
#Salida: la cadena al revés

from collections import deque


def invertir_palabras_con_pila(frase):
    pila = deque()
    # Fase 1: separar por espacios y apilar cada palabra
    for palabra in frase.split(" "):
        pila.append(palabra)

    # Fase 2: desapilar formando la salida
    palabras_invertidas = []
    while pila:
        palabras_invertidas.append(pila.pop())

    return " ".join(palabras_invertidas)


print(invertir_palabras_con_pila("Hola Mundo"))            # Mundo Hola
print(invertir_palabras_con_pila("Python es muy genial"))  # genial muy es Python

# Comparación con la versión pythonic (una línea)
print(" ".join("Hola Mundo".split(" ")[::-1]))             # Mundo Hola




#E2
#Verificar parentesis balanceados
#Dada una expresión con paréntesis, corchetes y llaves, verificar que estén correctamente balanceados y anidados.
#Entrada: una cadena de simbolos
#Proceso: usar una pila: apilar aperturas, al cerrar comprobar match
#Salida: True si está balanceado, False si no


from collections import deque


def paren_balanceado(s):
    pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}   # cierre → apertura

    for i, ch in enumerate(s):
        if ch in "([{":
            # Guardamos el carácter junto con su posición
            pila.append((ch, i))
        elif ch in ")]}":
            # Caso 1: cierre sin ninguna apertura pendiente
            if not pila:
                return False, f"Cierre '{ch}' sin apertura en la posición {i}"
            
            apertura, idx_apertura = pila.pop()
            # Caso 2: el cierre no coincide con la última apertura
            if apertura != parejas[ch]:
                return False, (
                    f"Cierre '{ch}' en posición {i} no coincide con "
                    f"'{apertura}' abierto en posición {idx_apertura}"
                )

    # Caso 3: terminó el texto pero quedaron aperturas sin cerrar
    if pila:
        apertura, idx_apertura = pila[0]
        return False, f"Apertura '{apertura}' en posición {idx_apertura} nunca se cerró"

    return True, "Balanceado correctamente"


# Pruebas
tests = ["()", "({[]})", "()[]{}", "(]", "({[)]}", "(((", "())"]
for t in tests:
    ok, mensaje = paren_balanceado(t)
    print(f"{t!r:10} → {ok!s:5} | {mensaje}")





#E3
#Decimal binario a pila 
#Convertir un número decimal a binario usando el algoritmo de divisiones sucesivas por 2. Los residuos se apilan y al final se leen al revés (desapilando).
#Entrada: un entero positivo
#Proceso: dividir sucesivamente entre 2, apilar residuos, luego desapilar
#Salida: el número en binario
from collections import deque


def binario_a_decimal(s):
    pila = deque()
    # Apilamos cada bit convertido a entero
    for bit in s:
        pila.append(int(bit))

    decimal = 0
    potencia = 0
    # Desapilamos de derecha a izquierda (2^0, 2^1, 2^2...)
    while pila:
        bit = pila.pop()
        decimal += bit * (2 ** potencia)
        potencia += 1

    return decimal


# Pruebas
for b in ["0", "1", "101", "1101", "1100100", "11111111"]:
    print(f"{b:>8} → {binario_a_decimal(b)}")

# Verificar con la nativa de Python
print(int("1101", 2))   # 13



#Propuestos
#P1 Ctrl+z de acciones
#Programa que use una pila para historial: opciones «Hacer acción», «Deshacer», «Ver historial».
#Entrada: hacer A, hacer B, deshacer
#Salida: Historial: [A]
from collections import deque

historial = deque()

while True:
    print("\n1.Hacer 2.Deshacer 3.Ver historial 4.Salir")
    op = input("Opción: ")

    if op == "1":
        accion = input("Descripción: ")
        historial.append(accion)
        print(f"Hecho: {accion}")

    elif op == "2":
        if not historial:
            print("Nada que deshacer")
        else:
            deshecha = historial.pop()
            print(f"Deshecho: {deshecha}")

    elif op == "3":
        if not historial:
            print("(vacío)")
        else:
            for i, a in enumerate(historial):
                print(f"  {i+1}. {a}")

    elif op == "4":
        break


#P2 Invertir orden de palabras en una frase
#Usar una pila para invertir el ORDEN de las palabras (no las letras).
#Entrada: s = "Hola Mundo desde Python"
#Salida: Python desde Mundo Hola

from collections import deque

def invertir_palabras(frase):
    pila = deque()
    for palabra in frase.split():
        pila.append(palabra)

    resultado = []
    while pila:
        resultado.append(pila.pop())
    return " ".join(resultado)


print(invertir_palabras("Hola Mundo desde Python"))
# Python desde Mundo Hola


#P4 Evaluar expresion postfija
#En notación postfija («polaca inversa»), los operadores van después: 3 4 + = 7. Evalúa una expresión como 3 4 + 5 * = 35.
#Entrada: "3 4 + 5 *"
#Salida: 35
from collections import deque

def evaluar_postfija(expr):
    pila = deque()
    for token in expr.split():
        if token in "+-*/":
            b = pila.pop()      # OJO al orden: b sale primero
            a = pila.pop()
            if token == "+": pila.append(a + b)
            elif token == "-": pila.append(a - b)
            elif token == "*": pila.append(a * b)
            elif token == "/": pila.append(a / b)
        else:
            pila.append(int(token))
    return pila.pop()


print(evaluar_postfija("3 4 +"))         # 7
print(evaluar_postfija("3 4 + 5 *"))     # 35
print(evaluar_postfija("5 1 2 + 4 * + 3 -"))  # 14
