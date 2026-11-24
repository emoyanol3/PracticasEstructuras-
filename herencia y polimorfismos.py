#E1
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

# Pero __str__ es distinto en cada uno:
print(p)                                          # Pasajero Ana [reserva: AB-1234] · 500 millas
print(e)                                          # Empleado Luis [EMP-01] · $1320.00
print(t)
