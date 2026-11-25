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

# Pero __str__ es distinto en cada uno:
print(p)                                          # Pasajero Ana [reserva: AB-1234] · 500 millas
print(e)                                          # Empleado Luis [EMP-01] · $1320.00
print(t)
