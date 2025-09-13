class empleado():
    def __init__(self, id, nombre, edad, tipo):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        

class Aministrativo(empleado):
    def __init__(self, id, nombre, edad, tipo, departamento):
        super().__init__(id, nombre, edad, tipo)
        self.departamento = departamento

class Operativo(empleado):
    def __init__(self, id, nombre, edad, tipo, turno):
        super().__init__(id, nombre, edad, tipo)   
        self.turno = turno

def crear_empleado(self):
    print('/*/*/*/*/*/*/*/*/*\n')
    print(f"Empleado registrado: {self.nombre}, ID: {self.id}, Edad: {self.edad}, Tipo: {self.tipo}")
    print('/*/*/*/*/*/*/*/*/*\n')
        
id = int(input("Ingrese el ID del empleado: "))
nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
tipo = input("Ingrese el tipo de empleado (Administrativo / Operativo): ")

uno = empleado(id, nombre, edad, tipo)

uno.crear_empleado()