
#E1 Insertar manteniendo el orden 
#Añadir a ListaEnlazada el método insertar_ordenado(data): si la lista está ordenada de menor a mayor, el nuevo dato debe quedar en su lugar correcto para que la lista siga ordenada.
#Entrada: una lista ordenada y un dato
#Proceso: encontrar el ANTERIOR al lugar correcto y reenganchar
#Salida: la misma lista, aún ordenada, con un nodo más

    # Método nuevo para la clase ListaEnlazada
    def insertar_ordenado(self, data):
        nuevo = Nodo(data)
        # Caso A: lista vacía, o el nuevo es menor que la cabeza → va al inicio
        if self.head is None or data < self.head.data:
            nuevo.next = self.head
            self.head = nuevo
        else:
            # Caso B: busco el ANTERIOR (el último con dato <= data)
            anterior = self.head
            while anterior.next is not None and anterior.next.data <= data:
                anterior = anterior.next
            nuevo.next = anterior.next      # paso 1: el nuevo agarra el resto
            anterior.next = nuevo           # paso 2: el anterior apunta al nuevo
        self.cantidad = self.cantidad + 1


    notas = ListaEnlazada()
for n in [30, 10, 40, 20]:
    notas.insertar_ordenado(n)
notas.listar()                # 10 → 20 → 30 → 40 → None
notas.insertar_ordenado(25)   # va entre 20 y 30
notas.insertar_ordenado(5)    # va al inicio
notas.insertar_ordenado(50)   # va al final
notas.listar()                # 5 → 10 → 20 → 25 → 30 → 40 → 50 → None



#E2 Eliminar todas  las apariciones de un valor
#Añadir el método eliminar_todos(data) que quite todos los nodos con ese dato (no solo el primero) y retorne cuántos borró. Debe funcionar aunque los repetidos estén seguidos o en la cabeza.
#Entrada: una lista y un dato
#Proceso: saltarme cada nodo con ese dato, contándolos
#Salida: la lista sin ese dato y cuántos se borraron

    # Método nuevo para la clase ListaEnlazada
    def eliminar_todos(self, data):
        borrados = 0
        # Fase 1: mientras la CABEZA tenga el dato, la quito
        while self.head is not None and self.head.data == data:
            self.head = self.head.next
            borrados = borrados + 1
        # Fase 2: reviso el resto mirando UN vagón adelante
        anterior = self.head
        while anterior is not None and anterior.next is not None:
            if anterior.next.data == data:
                anterior.next = anterior.next.next    # me salto el nodo...
                borrados = borrados + 1               # ...y NO avanzo
            else:
                anterior = anterior.next              # solo avanzo si no borré
        self.cantidad = self.cantidad - borrados
        return borrados
        l = ListaEnlazada()
for x in [3, 3, 7, 3, 3, 5, 3]:
    l.insertar_final(x)
l.listar()                    # 3 → 3 → 7 → 3 → 3 → 5 → 3 → None
print(l.eliminar_todos(3))    # 5
l.listar()                    # 7 → 5 → None
print(l.longitud())           # 2

#Propuestos
#P1 Contar nodos caminando
#Método contar() que retorne cuántos nodos hay, recorriéndolos uno a uno (sin usar self.cantidad). Sirve para comprobar que cantidad está bien llevada.
#Entrada: A → B → C → D
#Salida: 4

def contar(self):
    n = 0                         # contador
    actual = self.head
    while actual is not None:
        n = n + 1                 # cuento este vagón
        actual = actual.next
    return n


#P2 El mayor de la lista
#Método mayor() que retorne el dato más grande de la lista (o None si está vacía).
#Entrada: 4 → 9 → 2 → 7
#Salida: 9

def mayor(self):
    if self.head is None:
        return None               # lista vacía: no hay campeón
    campeon = self.head.data      # el primero es campeón provisional
    actual = self.head.next       # empiezo a comparar desde el segundo
    while actual is not None:
        if actual.data > campeon:
            campeon = actual.data # ¡nuevo campeón!
        actual = actual.next
    return campeon


#P3 Eliminar el ultimo 
#Método eliminar_final() que quite el último nodo y retorne su dato. Contempla la lista vacía y la lista de un solo nodo.
#Entrada: 4 → 9 → 2 → 7
#Salida: retorna 7; queda 4 → 9 → 2
def eliminar_final(self):
    if self.head is None:
        print("Lista vacía")
        return None
    if self.head.next is None:            # un solo nodo: la lista queda vacía
        dato = self.head.data
        self.head = None
        self.cantidad = self.cantidad - 1
        return dato
    penultimo = self.head
    while penultimo.next.next is not None:    # miro DOS vagones adelante
        penultimo = penultimo.next
    dato = penultimo.next.data
    penultimo.next = None                 # el penúltimo pasa a ser el último
    self.cantidad = self.cantidad - 1
    return dato


#P4 Insertar después de un valor  
#Método insertar_despues(referencia, data) que busque el primer nodo con referencia y enganche un nodo nuevo justo después. Si la referencia no existe, avisa.
#Entrada: insertar_despues(9, 5) en 4 → 9 → 2
#Salida: 4 → 9 → 5 → 2

def insertar_despues(self, referencia, data):
    actual = self.head
    while actual is not None and actual.data != referencia:
        actual = actual.next
    if actual is None:                    # recorrí todo y no estaba
        print(referencia, "no existe")
        return
    nuevo = Nodo(data)
    nuevo.next = actual.next              # paso 1: el nuevo agarra el resto
    actual.next = nuevo                   # paso 2: actual apunta al nuevo
    self.cantidad = self.cantidad + 1


#P5 El k ésimo desde el final 
#Método desde_final(k) que retorne el dato del nodo k-ésimo contando desde el final (k=1 es el último), sin usar cantidad.
#Entrada: A → B → C → D → E, k = 2
#Salida: D
def desde_final(self, k):
    # Técnica: dos punteros. Adelanto uno k pasos y luego avanzo los dos juntos.
    if k <= 0:
        return None
    adelantado = self.head
    for _ in range(k):
        if adelantado is None:
            return None               # k mayor que la longitud
        adelantado = adelantado.next
    # Ahora el segundo puntero sale desde head hasta que adelantado llegue a None
    detras = self.head
    while adelantado is not None:
        adelantado = adelantado.next
        detras = detras.next
    return detras.data


#P6 Detectar un ciclo 
#Método tiene_ciclo() que retorne True si algún nodo apunta a uno anterior (formando un ciclo, como el error de invertir las líneas al insertar). Usa el algoritmo de Floyd (la liebre y la tortuga).
#Entrada: A → B → C → D → (vuelve a B)
#Salida: True

def tiene_ciclo(self):
    """Floyd: la tortuga avanza 1, la liebre 2. Si se encuentran, hay ciclo."""
    tortuga = self.head
    liebre = self.head
    while liebre is not None and liebre.next is not None:
        tortuga = tortuga.next
        liebre = liebre.next.next
        if tortuga is liebre:
            return True
    return False

# Prueba: crear un ciclo a mano
lista = ListaEnlazada()
for x in ["A", "B", "C", "D"]:
    lista.insertar_final(x)
print(lista.tiene_ciclo())          # False

d = lista.head.next.next.next       # A → B → C → D
d.next = lista.head.next            # D → B  (¡ciclo!)
print(lista.tiene_ciclo())          # True
