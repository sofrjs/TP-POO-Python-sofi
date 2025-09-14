#Herencia

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado) 
        
#Polimorfismo
class Persona:
    def avanza(self):
        print("La persona avanza caminando.")

class Ciclista(Persona):
    def avanza(self):
        print("El ciclista avanza pedaleando.")
        
# --- Prueba de Herencia ---
print("--- Probando Herencia: Rectángulo y Cuadrado ---")
mi_rectangulo = Rectangulo(4, 6)
print(f"El área del rectángulo es: {mi_rectangulo.area()}")

mi_cuadrado = Cuadrado(5)
# El Cuadrado hereda el método area() del Rectángulo.
print(f"El área del cuadrado es: {mi_cuadrado.area()}")

# --- Prueba de Polimorfismo ---
print("\n--- Probando Polimorfismo: Persona y Ciclista ---")
mi_persona = Persona()
mi_ciclista = Ciclista()

# Cada objeto responde de forma diferente al mismo método 'avanza()'
mi_persona.avanza()
mi_ciclista.avanza()