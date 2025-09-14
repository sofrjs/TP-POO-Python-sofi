class Hotel:
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def anadir_huespedes(self, cantidad):
        if self.huespedes + cantidad <= self.numero_maximo_de_huespedes:
            self.huespedes += cantidad
            print(f"Se han añadido {cantidad} huéspedes. Ocupación actual: {self.huespedes}.")
        else:
            print(f"No se puede añadir a {cantidad} huéspedes. La capacidad máxima es de {self.numero_maximo_de_huespedes} y ya hay {self.huespedes} huéspedes.")

    def checkout(self, cantidad):
        if self.huespedes - cantidad >= 0:
            self.huespedes -= cantidad
            print(f"Han salido {cantidad} huéspedes. Ocupación actual: {self.huespedes}.")
        else:
            print(f"No se puede realizar el checkout de {cantidad} huéspedes. Solo hay {self.huespedes} huéspedes.")

    def ocupacion_total(self):
        return (f"El hotel tiene actualmente {self.huespedes} huéspedes, con una capacidad máxima de {self.numero_maximo_de_huespedes} y {self.lugares_de_estacionamiento} lugares de estacionamiento.")

# - Probar el funcionamiento -

# Crear una instancia del Hotel
print("--- Hotel ---")
mi_hotel = Hotel(50, 20)
print(mi_hotel.ocupacion_total())

print("\n--- Añadiendo 35 huéspedes ---")
mi_hotel.anadir_huespedes(35)
print(mi_hotel.ocupacion_total())

print("\n--- Intentando añadir 20 huéspedes (se excede la capacidad) ---")
mi_hotel.anadir_huespedes(20)
print(mi_hotel.ocupacion_total())

print("\n--- Realizando el checkout de 15 huéspedes ---")
mi_hotel.checkout(15)
print(mi_hotel.ocupacion_total())

print("\n--- Intentando un checkout de 30 huéspedes (más de los que hay) ---")
mi_hotel.checkout(30)
print(mi_hotel.ocupacion_total())