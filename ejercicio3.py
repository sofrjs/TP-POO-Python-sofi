class Vehiculo:
    def __init__(self, placa, marca):
        self.placa = placa  
        self.marca = marca 

    def getPlaca(self):
        return self.placa

    def getMarca(self):
        return self.marca

    def mostrarVehiculo(self):
        print(f"La placa del vehículo es: {self.getPlaca()}")
        print(f"La marca del vehículo es: {self.getMarca()}")

# --- Entrada de datos por teclado y uso de la clase ---

# Solicitar al usuario que ingrese la placa y la marca
print("--- Ingresa los datos del vehículo ---")
placa_ingresada = input("Ingresa la placa del vehículo: ")
marca_ingresada = input("Ingresa la marca del vehículo: ")

# Crear una instancia del objeto Vehiculo
mi_vehiculo = Vehiculo(placa_ingresada, marca_ingresada)

print("\n--- Datos del vehículo registrado ---")
mi_vehiculo.mostrarVehiculo()