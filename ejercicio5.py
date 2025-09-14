class Empleado:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombreCompleto(self):
        return f"{self._nombre} {self._apellido}"

    @nombreCompleto.setter
    def nombreCompleto(self, nuevo_nombre):
        print("Estableciendo el nuevo nombre completo...")
        partes = nuevo_nombre.split()
        if len(partes) >= 2:
            self._nombre = partes[0]
            self._apellido = " ".join(partes[1:])

# 1. Crear una instancia del Empleado
print("--- Creación del empleado ---")
mi_empleado = Empleado("Ana", "Gómez")

# 2. Consultar el nombre completo usando la propiedad
print(f"Nombre inicial: {mi_empleado.nombreCompleto}")

# 3. Modificar el nombre completo usando la propiedad
print("\n--- Modificando el nombre del empleado ---")
mi_empleado.nombreCompleto = "Pedro Pérez"

# 4. Consultar el nombre completo modificado
print(f"Nombre modificado: {mi_empleado.nombreCompleto}")