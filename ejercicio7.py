class Estudiante:
    def __init__(self, nombres, apellidos, cedula, carrera, edad):
        self._nombres = nombres
        self._apellidos = apellidos
        self._cedula = cedula
        self._carrera = carrera
        self._edad = edad

    def getNombres(self):
        return self._nombres

    def getApellidos(self):
        return self._apellidos

    def getCedula(self):
        return self._cedula

    def getCarrera(self):
        return self._carrera

    def getEdad(self):
        return self._edad

    def imprimirEstudiante(self):
        print("\n--- Datos del Estudiante ---")
        print(f"Nombres: {self.getNombres()}")
        print(f"Apellidos: {self.getApellidos()}")
        print(f"Cédula: {self.getCedula()}")
        print(f"Carrera: {self.getCarrera()}")
        print(f"Edad: {self.getEdad()} años")

# --- Interacción con el usuario ---

print("Por favor, ingresa los datos del estudiante:")
nombres = input("Nombres: ")
apellidos = input("Apellidos: ")
cedula = input("Cédula: ")
carrera = input("Carrera: ")
edad = int(input("Edad: ")) 

mi_estudiante = Estudiante(nombres, apellidos, cedula, carrera, edad)
mi_estudiante.imprimirEstudiante()