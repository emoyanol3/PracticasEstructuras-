#E1 clase pasajero 
#Crear la clase Pasajero con nombre, cédula y edad. Crear tres instancias y mostrarlas.
#Entrada: los datos de tres pasajeros
#Proceso: definir la clase, luego instanciar
#Salida: los tres pasajeros formateados


class Pasajero:
  def __init__(self, nombre, cedula, edad):
    self.nombre=nombre
    self.cedula=cedula
    self.edad=edad

  def __str__(self):
    return (f"Nombre: {self.nombre}, Cedula: {self.cedula}, edad: {self.edad}")

p1 = Pasajero("Ana", "0912345678", 28)
p2 = Pasajero("Luis", "0987654321", 35)
p3 = Pasajero("Diana", "0923456789", 22)

print(p1)
print(p2)
print(p3)



#E1 Adicional clase pasajero 
#Crear la clase Pasajero con nombre, cédula y edad. Crear tres instancias y mostrarlas. Añade un método cumplir_anios() que sume 1 a la edad.
#Entrada: los datos de tres pasajeros
#Proceso: definir la clase, luego instanciar
#Salida: los tres pasajeros formateados


class Pasajero:
  def __init__(self, nombre, cedula, edad):
    self.nombre=nombre
    self.cedula=cedula
    self.edad=edad

  def cumplir_anios(self, anio):
    self.edad+=anio


  def __str__(self):
    return (f"Nombre: {self.nombre}, Cedula: {self.cedula}, edad: {self.edad}")


p1 = Pasajero("Ana", "0912345678", 28)
p2 = Pasajero("Luis", "0987654321", 35)
p3 = Pasajero("Diana", "0923456789", 22)

p1.cumplir_anios(2)
print(p1)
print(p2)
print(p3)


#E2 clase cuenta bancaria
#Crear CuentaBancaria con métodos depositar, retirar, saldo y __str__. El saldo empieza en 0. No se puede retirar más de lo que hay.
#Entrada: movimientos de la cuenta
#Proceso: métodos que modifican el estado interno
#Salida: el saldo tras cada operación

class CuentaBancaria:
    def __init__(self, nombre, numero):
        self.nombre=nombre
        self.numero = numero
        self._saldo = 0  

    def depositar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return
        
        self._saldo += monto
        print(f"Depósito de ${monto}. Saldo de {self.nombre}: ${self._saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return
            
        if monto > self._saldo:
            print(f"Saldo insuficiente (tiene ${self._saldo})")
            return
            
        self._saldo -= monto
        print(f"Retiro de ${monto}. Saldo de {self.nombre}: ${self._saldo}")

    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"Cuenta de {self.nombre}, # cuenta: {self.numero}, saldo: ${self._saldo}"

# --- Uso ---
c = CuentaBancaria("Eduard","001")
c.depositar(200)         # Depósito de $100. Saldo: $100
c.retirar(30)            # Retiro de $30. Saldo: $70
c.retirar(200)           # Saldo insuficiente (tiene $70)
print(c)                 # Cuenta 001: $70
print(c.saldo())         # 70



#E2 Adicional clase cuenta bancaria#Crear CuentaBancaria con métodos depositar, retirar, saldo y __str__. El saldo empieza en 0. No se puede retirar más de lo que hay. #Añade historial: una lista donde cada operación añade un string tipo '+100', '-30'. Método ver_historial().
#Entrada: movimientos de la cuenta
#Proceso: métodos que modifican el estado interno
#Salida: el saldo tras cada operación

class CuentaBancaria:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self._saldo = 0  
        self._historial = []  

    def depositar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return
        
        self._saldo += monto
        self._historial.append(f"+{monto}")  
        print(f"Depósito de ${monto}. Saldo de {self.nombre}: ${self._saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return
            
        if monto > self._saldo:
            print(f"Saldo insuficiente (tiene ${self._saldo})")
            return
            
        self._saldo -= monto
        self._historial.append(f"-{monto}") 
        print(f"Retiro de ${monto}. Saldo de {self.nombre}: ${self._saldo}")

    def saldo(self):
        return self._saldo

    def ver_historial(self):
        if not self._historial:
            print("No hay movimientos registrados.")
            return
        print(f"Historial de {self.nombre}: {self._historial}")

    def __str__(self):
        return f"Cuenta de {self.nombre}, # cuenta: {self.numero}, saldo: ${self._saldo}"



c = CuentaBancaria("Eduard", "001")

c.depositar(200)  
c.retirar(30)           

print(c)                 
print(f"Saldo actual: ${c.saldo()}")  

c.ver_historial()      



#E3 Clase Producto 
#con nombre, precio y stock. Métodos: vender(cantidad) (reduce stock si hay), reabastecer(cantidad), valor_inventario() (precio × stock).#Entrada: productos y sus operaciones#Proceso: encapsular stock y precio#Salida: valor del inventario y estado del productoc
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = precio if precio >= 0 else 0
        self._stock = stock if stock >= 0 else 0

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no válida")
            return
            
        if cantidad > self._stock:
            print(f"Sin stock suficiente disponible de {self.nombre}")
            return
            
        self._stock -= cantidad
        print(f"Vendidas {cantidad} unidades de {self.nombre}. Stock restante: {self._stock}")

    def reabastecer(self, cantidad):
        if cantidad <= 0:
            print("Ingrese una cantidad válida")
            return
            
        self._stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self._stock}")

    def valor_inventario(self):
        # Si el stock es 0, el valor del inventario simplemente es $0.00
        return self._precio * self._stock

    def __str__(self):
        return f"{self.nombre} - ${self._precio:.2f} - stock: {self._stock}"


# --- Uso y Pruebas ---
leche = Producto("Leche", 1.20, 10)
pan = Producto("Pan", 0.50, 30)

print(leche)                               
leche.vender(3)  
print("===============")
print(f"Valor del inventario de {leche.nombre}: ${leche.valor_inventario():.2f}")  
leche.vender(20)  


#E3 Adicional Clase Producto 

#Amplíalo con un método de clase total_inventario(productos) que sume los valores de una #lista de productos.
#con nombre, precio y stock. Métodos: vender(cantidad) (reduce stock si hay), reabastecer(cantidad), valor_inventario() (precio × stock).
#Entrada: productos y sus operaciones
#Proceso: encapsular stock y precio
#Salida: valor del inventario y estado del producto

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = precio if precio >= 0 else 0
        self._stock = stock if stock >= 0 else 0

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no válida")
            return
            
        if cantidad > self._stock:
            print(f"Sin stock suficiente disponible de {self.nombre}")
            return
            
        self._stock -= cantidad
        print(f"Vendidas {cantidad} unidades de {self.nombre}. Stock restante: {self._stock}")

    def reabastecer(self, cantidad):
        if cantidad <= 0:
            print("Ingrese una cantidad válida")
            return
            
        self._stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self._stock}")

    def valor_inventario(self):
        return self._precio * self._stock

    @classmethod
    def total_inventario(cls, productos):
        """Suma el valor individual del inventario de cada producto en la lista."""
        return sum(producto.valor_inventario() for producto in productos)

    def __str__(self):
        return f"{self.nombre} - ${self._precio:.2f} - stock: {self._stock}"


# --- Uso y Pruebas ---
leche = Producto("Leche", 1.20, 10)
pan = Producto("Pan", 0.50, 30)
queso = Producto("Queso", 2.50, 5)

print(leche)                                           
leche.vender(3)  
print("===============")
print(f"Valor del inventario de {leche.nombre}: ${leche.valor_inventario():.2f}")  
leche.vender(20)

print("\n=== TOTAL DEL INVENTARIO ===")
lista_productos = [leche, pan, queso]

# Se puede llamar directamente desde la Clase:
total = Producto.total_inventario(lista_productos)
print(f"Valor total de todos los productos almacenados: ${total:.2f}")




#Ejercicios propuestos            
   
#P1 Clase rectangulo                           
#Clase Rectangulo con base y altura. Métodos area(), perimetro() y __str__.
#Entrada: Base, altura
#Proceso: Multiplicar base * altura
#Salida: area, perimetro

class Rectangulo:
  def __init__(self, base, altura):
    self.base=base
    self.altura=altura

  def area(self):
    return self.base*self.altura

  def perimetro(self):
    return 2*(self.base+self.altura)

  def __str__(self):
    return (f"Area: {self.area()}, Perimetro: {self.perimetro()} ")

r=Rectangulo(5,3)
print (r)
print (f" Area: {r.area()} ")


#P2 Clase circulo
#Clase con radio y métodos area() (π·r²) y circunferencia() (2·π·r). Usa math.pi.
#Entrada: pi, radio
#Proceso: formular area y circunferencia
#Salida: area circunferencia

import math

class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return math.pi * (self.radio**2)
    def circunferencia(self):
        return (2*math.pi*self.radio)

    def __str__(self):
        return (f"Area: {self.area():.2f}, circunferencia: {self.circunferencia():.2f} ")

c=Circulo(5)
print(c)


#P3 Clase Estudiante con nombre y una lista de notas. 
#Métodos: agregar_nota(n), promedio(), aprobado() (True si promedio ≥ 7).

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []          # lista vacía inicial

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 7

    def __str__(self):
        return f"{self.nombre}: {self.notas} → prom={self.promedio():.2f}"

# --- Uso ---
ana = Estudiante("Ana")
for n in [8, 6, 9]:
    ana.agregar_nota(n)
print(ana)
print(f"Aprobado: {ana.aprobado()}")


 
#P4 Clase Vehiculo 
#con marca, modelo y km recorridos (inicialmente 0). Método recorrer(km) que suma al odómetro. Método necesita_mantenimiento() que retorna True cada 10 000 km.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0
        self._ultimo_mantenimiento = 0

    def recorrer(self, distancia):
        self.km += distancia

    def necesita_mantenimiento(self):
        return (self.km - self._ultimo_mantenimiento) >= 10000

    def hacer_mantenimiento(self):
        self._ultimo_mantenimiento = self.km
        print(f"Mantenimiento hecho a los {self.km} km")

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.km} km"

auto = Vehiculo("Toyota", "Corolla")
auto.recorrer(15000)
print(auto)                                       # Toyota Corolla - 15000 km
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")
auto.hacer_mantenimiento()                        # se resetea el contador
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")

