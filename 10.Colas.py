#E1 Fila  de atención de un banco
#Simular una fila de banco: los clientes llegan (encolar) y el cajero los atiende en orden (desencolar).
#Entrada: opción del menú y datos
#Proceso: menú con encolar/desencolar/frente
#Salida: estado de la fila y siguiente en atención

from collections import deque

cola = deque()

while True:
    print("\n1.Llega cliente 2.Atender 3.Ver frente 4.Ver toda la cola 5.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        cola.append(nom)
        print(f"{nom} entró a la fila. {len(cola)} clientes en espera.")

    elif op == "2":
        if not cola:
            print("No hay clientes")
        else:
            atendido = cola.popleft()
            print(f"Atendiendo a: {atendido}. Quedan {len(cola)}.")

    elif op == "3":
        if not cola:
            print("Fila vacía")
        else:
            print(f"Siguiente: {cola[0]}")

    elif op == "4":
        if not cola:
            print("(vacía)")
        else:
            for i, c in enumerate(cola):
                marca = " ← siguiente" if i == 0 else ""
                print(f"  {i+1}. {c}{marca}")

    elif op == "5":
        break


#E2 Simuladdor de impresora
#Un sistema recibe documentos para imprimir. Los procesa en orden de llegada. Cada documento tarda su número de páginas × 2 segundos.
#Entrada: trabajos con nombre y páginas
#Proceso: cola de trabajos, procesar en orden
#Salida: estado y tiempos

from collections import deque

def procesar_impresora(trabajos):
    cola = deque(trabajos)
    tiempo_total = 0

    while cola:
        nombre, paginas = cola.popleft()      # FIFO: el primero en llegar
        tiempo = paginas * 2
        tiempo_total += tiempo
        print(f"Imprimiendo {nombre}: {paginas} páginas → {tiempo}s "
              f"(acumulado {tiempo_total}s)")

    return tiempo_total


# --- Uso ---
trabajos = [
    ("Contrato.pdf", 5),
    ("Recibo.pdf", 2),
    ("Manual.pdf", 10),
]

total = procesar_impresora(trabajos)
print(f"\nTiempo total: {total}s")

#E3 Cola de prioridad simple
#Extender la cola para que acepte una prioridad. Los de mayor prioridad se atienden primero, y entre iguales, por orden de llegada.
#Entrada: elementos con nombre y prioridad
#Proceso: usar múltiples deques (una por nivel de prioridad)
#Salida: el orden correcto de atención

from collections import deque

class ColaPrioridad:
    def __init__(self, niveles=3):
        # Un deque por cada nivel (índice = prioridad, más alto = más urgente)
        self.niveles = niveles
        self.colas = [deque() for _ in range(niveles + 1)]

    def encolar(self, valor, prioridad):
        if not 0 < prioridad <= self.niveles:
            raise ValueError(f"Prioridad entre 1 y {self.niveles}")
        self.colas[prioridad].append(valor)

    def desencolar(self):
        """Saca el de mayor prioridad; entre iguales, el más antiguo."""
        # Recorremos de la prioridad más alta a la más baja
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                return self.colas[i].popleft()
        raise IndexError("Cola vacía")

    def __str__(self):
        s = []
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                s.append(f"  P{i}: {list(self.colas[i])}")
        return "\n".join(s) if s else "(vacía)"


# --- Uso ---
cp = ColaPrioridad(3)
cp.encolar("Ana", 1)
cp.encolar("Luis", 3)
cp.encolar("Diana", 1)
cp.encolar("Beto", 2)

print(cp)
# P3: ['Luis']
# P2: ['Beto']
# P1: ['Ana', 'Diana']

# Atender en orden
while True:
    try:
        print("Atendiendo:", cp.desencolar())
    except IndexError:
        break
# Luis / Beto / Ana / Diana

#Propuestos
#P1 Fila con tickets numerados
#Simulador con tickets automáticos: al llegar un cliente se le asigna un número (1, 2, 3...). Al atender, se llama el siguiente.
#Entrada: 3 llegadas, 2 atenciones
#Salida: atendidos 1 y 2; quedan: [ticket 3]

from collections import deque

cola = deque()
proximo = 1

while True:
    print("\n1.Llega 2.Atender 3.Ver cola 4.Salir")
    op = input("Opción: ")

    if op == "1":
        cola.append(proximo)
        print(f"Ticket {proximo} asignado. {len(cola)} en espera.")
        proximo += 1
    elif op == "2":
        if not cola:
            print("Sin clientes")
        else:
            print(f"Turno {cola.popleft()}")
    elif op == "3":
        print(list(cola))
    elif op == "4":
        break

#P2 Turno rotativo
#Se rotan turnos entre jugadores. Al «terminar el turno», el jugador vuelve al final de la cola. Muestra 10 turnos consecutivos.
#Entrada: jugadores = [A, B, C]
#Salida: A, B, C, A, B, C, A, B, C, A

from collections import deque

jugadores = deque(["Ana", "Beto", "Carlos"])

for turno in range(10):
    actual = jugadores.popleft()      # sale del frente
    print(f"Turno {turno+1}: {actual}")
    jugadores.append(actual)          # vuelve al final



#P3 Cola con máximo historicp
#Cola normal, pero con un método adicional maximo_visto() que retorna el máximo valor que HA PASADO por la cola (aunque ya haya salido).
#Entrada: encola 5, 3, 8, 2 y desencola todo
#Salida: Máximo visto: 8

from collections import deque

class ColaConMax:
    def __init__(self):
        self._datos = deque()
        self._max_visto = float("-inf")

    def encolar(self, v):
        self._datos.append(v)
        if v > self._max_visto:
            self._max_visto = v

    def desencolar(self):
        if not self._datos:
            raise IndexError("vacía")
        return self._datos.popleft()

    def maximo_visto(self):
        return self._max_visto


c = ColaConMax()
for x in [5, 3, 8, 2]:
    c.encolar(x)
while c._datos:
    print(c.desencolar())
print("Máximo visto:", c.maximo_visto())



#P4 Simulador de café, dos cajas
#Los clientes llegan a UNA cola. Hay 2 cajas; cada una toma al primero de la cola cuando queda libre. Cada cliente tarda entre 30 y 90 segundos. Simula 10 clientes.
#Entrada: 10 clientes
#Salida: Tiempo total: ~350s
import random
from collections import deque

random.seed(42)                     # para reproducibilidad
cola = deque([f"Cliente-{i+1}" for i in range(10)])

# Dos cajas: cada una guarda (cliente, tiempo_restante) o None si libre
cajas = [None, None]

segundo = 0

while cola or any(cajas):
    # Cada caja libre agarra al primero
    for i in range(2):
        if cajas[i] is None and cola:
            cliente = cola.popleft()
            tiempo = random.randint(30, 90)
            cajas[i] = [cliente, tiempo]
            print(f"[{segundo}s] Caja {i+1}: atendiendo a {cliente} ({tiempo}s)")

    # Cada caja ocupada trabaja 1 segundo
    for i in range(2):
        if cajas[i]:
            cajas[i][1] -= 1
            if cajas[i][1] == 0:
                print(f"[{segundo+1}s] Caja {i+1}: terminó con {cajas[i][0]}")
                cajas[i] = None

    segundo += 1

print(f"\nTiempo total: {segundo}s")
