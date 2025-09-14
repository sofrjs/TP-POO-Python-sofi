class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    def responder_saludo(self, otra_persona):
        print(f"Hola {otra_persona.nombre}, me llamo {self.nombre} y tengo {self.edad} años.")


# Instanciar a dos personas
persona1 = Persona("Guido", 36)
persona2 = Persona("Patricio", 39)

persona1.saludar()
persona2.responder_saludo(persona1)