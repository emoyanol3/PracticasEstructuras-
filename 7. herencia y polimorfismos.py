#E1 Herencia y polimorfismo
#Modela una empresa aérea con Persona como clase base y Pasajero y Empleado como hijas. Cada hija añade su propio atributo y método.
#Entrada: los datos de una persona más los específicos
#Proceso: clase base con lo común, hijas con lo específico
#Salida: presentación adaptada a cada tipo

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):
        print(f"Soy {self.nombre}, cédula {self.cedula}")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Pasajero(Persona):
    def __init__(self, nombre, cedula, codigo_reserva):
        super().__init__(nombre, cedula)         # inicializa lo del padre
        self.codigo_reserva = codigo_reserva
        self.millas = 0

    def sumar_millas(self, m):
        self.millas += m

    def __str__(self):
        return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}] · {self.millas} millas"


class Empleado(Persona):
    def __init__(self, nombre, cedula, codigo_emp, salario):
        super().__init__(nombre, cedula)
        self.codigo_emp = codigo_emp
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)

    def __str__(self):
        return f"Empleado {self.nombre} [{self.codigo_emp}] · ${self.salario:.2f}"

class Tripulante(Empleado):
  def __init__(self, nombre, cedula, codigo_emp, salario, rol):
    super().__init__(nombre,cedula, codigo_emp, salario)
    self.rol=rol
    
  def __str__(self):
    return f"Tripulante: {self.nombre}, Código: [{self.codigo_emp}] Salario: ${self.salario:.2f}, Rol: {self.rol} "


# --- Uso ---
p = Pasajero("Ana", "0912345678", "AB-1234")
e = Empleado("Luis", "0987654321", "EMP-01", 1200)
t = Tripulante("Miguel", "0987654321","EMP-33", 6000,"Capitán")

p.sumar_millas(500)
e.aumentar_salario(10)

# Ambos heredan presentarse():
p.presentarse()                                   # Soy Ana, cédula 0912345678
e.presentarse()                                   # Soy Luis, cédula 0987...
t.presentarse()



#E2 Polimorfismo con figuras 
#Entrada: figuras de distinta forma
#Proceso: una lista mixta de figuras
#Salida: las áreas de todas, con un mismo bucle

import math


class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar area()")

    def perimetro(self):
        raise NotImplementedError("Cada figura debe implementar perimetro()")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        # Un cuadrado es un rectángulo donde base y altura son iguales
        super().__init__(lado, lado)


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Triangulo(Figura):
    def __init__(self, base, altura, lado1=None, lado2=None):
        self.base = base
        self.altura = altura
        # Si no se especifican los otros lados, asume triángulo rectángulo (base y altura como catetos)
        if lado1 is None or lado2 is None:
            self.lado1 = altura
            self.lado2 = math.hypot(base, altura)
        else:
            self.lado1 = lado1
            self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2


# --- Uso polimórfico ---
figuras = [
    Rectangulo(5, 3),
    Cuadrado(4),
    Circulo(5),
    Triangulo(4, 3)  # Triángulo rectángulo 3-4-5
]

for f in figuras:
    print(f"{type(f).__name__} -> Área: {f.area():.2f} | Perímetro: {f.perimetro():.2f}")

# Y podemos sumar todas
total_area = sum(f.area() for f in figuras)
total_perimetro = sum(f.perimetro() for f in figuras)

print(f"\nÁrea total: {total_area:.2f}")
print(f"Perímetro total: {total_perimetro:.2f}")


#Propuestos 
#P1 Base Vehiculo(marca, modelo). Hija Auto con puertas. Hija Moto con cilindraje. Ambas tienen __str__ propio.
#Entrada: auto = Auto('Toyota', 'Corolla', 4)
#Proceso aplicar herencia y polimorfismo
#Salida: Toyota Corolla — 4 puertas

# P1
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def __str__(self):
        return f"{super().__str__()} — {self.puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"{super().__str__()} — {self.cilindraje}cc"


# --- Uso ---
print("=======================")
print("Lista de coches y motos")
print("=======================")

auto = Auto("Mercedes", "280s", 4)
auto2 = Auto("BMW", "E38", 2)
moto = Moto("Suzuki", "CR", 600)

print("Autos")
print("=======================")
for v in [auto, auto2]:
    print(v)

print("\nMotos")
print("=======================")
for m in [moto]:
    print(m)




 
#P2 Base Animal(nombre) con método hablar() que dice «(sonido)». Cada hija sobrescribe con su propio sonido.
#Entrada: para 3 animales
#Proceso; Aplicar herencia y polimorfismo
#Salida: Rex: Guau, Felix: Miau, Piolín: Pío


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre}: (sonido)")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre}: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre}: Miau")

class Ave(Animal):
    def hablar(self):
        print(f"{self.nombre}: Pío pío")
      
class Vaca(Animal):
    def hablar(self):
        print(f"{self.nombre}: Muuuuuuu")
      
class Leon(Animal):
    def hablar(self):
      print(f"{self.nombre}: Raawwwwwww ")

# Uso polimórfico
print("Animales y sus sonidos")
print("-----------------------")
animales = [Perro("Rex"), Gato("Felix"), Ave("Piolín"), Vaca("Lola"), Leon("Simba")]
for a in animales:
    a.hablar()


#P3 
#Base Empleado(nombre) con método abstracto sueldo_mensual(). EmpleadoPorHoras calcula sueldo por horas trabajadas × tarifa. EmpleadoFijo tiene sueldo fijo.
#Entrada: por_horas: 160h × 8, fijo: 1500
#Proceso: Aplicar herencia y polimorfismo
#Salida: 1280.00, 1500.00

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def sueldo_mensual(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.nombre}: ${self.sueldo_mensual():.2f}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def sueldo_mensual(self):
        return self.horas * self.tarifa


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo

    def sueldo_mensual(self):
        return self.sueldo


# Nómina polimórfica
empleados = [
    EmpleadoPorHoras("Ericka", 100, 8),
    EmpleadoPorHoras("Miguel", 160, 8),
    EmpleadoFijo("Heriberto", 1500)
]

nomina = 0
for e in empleados:
    print(e)
    nomina += e.sueldo_mensual()

print(f"Total nómina: ${nomina:.2f}")


# Pero __str__ es distinto en cada uno:
print(p)                                          # Pasajero Ana [reserva: AB-1234] · 500 millas
print(e)                                          # Empleado Luis [EMP-01] · $1320.00
print(t)
