class Lavadora:
    def __init__(self):
        pass

    def _llenar_tanque_de_agua(self, temperatura):
        print(f"Llenando el tanque con agua {temperatura}...")
    
    def _lavar(self):
        print("Lavando la ropa...")
        print("¡El lavado ha terminado!")

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._lavar()


# Crear una instancia de la lavadora
mi_lavadora = Lavadora()

# Llamar al método público "lavar"
print("--- Lavando con agua caliente ---")
mi_lavadora.lavar()

print("\n--- Lavando con agua fría ---")
mi_lavadora.lavar(temperatura='fria')