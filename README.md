# Trabajo Práctico: Programación Orientada a Objetos en Python

## 📌 Consigna
El objetivo de este trabajo práctico es aplicar los conceptos fundamentales de **Programación Orientada a Objetos (POO)** en Python, trabajando con **clases, objetos, atributos, métodos, herencia, polimorfismo, encapsulación y abstracción**.

## 🧩 Contenidos a trabajar
- Definición de clases y objetos
- Atributos y métodos
- Métodos constructores (`__init__`)
- Encapsulación (getters, setters, propiedades)
- Abstracción (métodos privados y públicos)
- Herencia
- Polimorfismo
- Sobrecarga de métodos

## 📂 Entregables
Forkea el repositorio desde https://github.com/FabioDrizZt/TP-POO-Python/
Cada ejercicio debe resolverse en un archivo `.py` independiente.  
Ejemplo: `ejercicio1.py`, `ejercicio2.py`, etc.  

Además, incluir un archivo `main.py` que permita probar la ejecución de cada clase desarrollada.

---

## ✍️ Ejercicios

### **Ejercicio 1: Clase Persona**
1. Crear una clase `Persona` con atributos `nombre` y `edad`.
2. Definir un método `saludar()` que imprima:  
   `"Hola, me llamo <nombre> y tengo <edad> años."`
3. Instanciar al menos **dos personas** y hacer que se saluden entre sí.

---

### **Ejercicio 2: Clase Hotel**
1. Crear una clase `Hotel` con:
   - `numero_maximo_de_huespedes`
   - `lugares_de_estacionamiento`
   - `huespedes` (inicialmente 0)
2. Métodos:
   - `anadir_huespedes(cantidad)`
   - `checkout(cantidad)`
   - `ocupacion_total()`
3. Probar el funcionamiento creando un hotel de 50 huéspedes y 20 estacionamientos.

---

### **Ejercicio 3: Clase Vehículo**
1. Crear una clase `Vehiculo` con atributos `placa` y `marca`.
2. Incluir métodos de acceso (`getPlaca`, `getMarca`) y un método transaccional `mostrarVehiculo()`.
3. Permitir al usuario ingresar los datos por teclado y mostrar el vehículo.

---

### **Ejercicio 4: Abstracción con Lavadora**
1. Implementar la clase `Lavadora` con un método público `lavar()` y métodos privados `_llenar_tanque_de_agua()` y `_lavar()`.
2. Simular el proceso de lavado mostrando mensajes por consola.

---

### **Ejercicio 5: Encapsulación con Empleado**
1. Crear la clase `Empleado` con atributos `nombre` y `apellido`.
2. Implementar una propiedad `nombreCompleto` que pueda ser consultada y modificada con `@property` y `@setter`.
3. Probar la creación y modificación de un empleado.

---

### **Ejercicio 6: Herencia y Polimorfismo**
1. Crear una clase `Rectangulo` con atributos `base` y `altura`, y un método `area()`.
2. Crear la subclase `Cuadrado` que herede de `Rectangulo`.
3. Crear una clase `Persona` con un método `avanza()`.
4. Crear la subclase `Ciclista` que sobrescriba el método `avanza()`.
5. Probar instanciando objetos de cada clase y llamando a sus métodos.

---

### **Ejercicio 7: Clase Estudiante**
1. Crear la clase `Estudiante` con atributos:
   - `nombres`, `apellidos`, `cedula`, `carrera`, `edad`.
2. Definir métodos de acceso (`getNombres`, `getApellidos`, etc.).
3. Crear un método `imprimirEstudiante()` que muestre todos los datos.
4. Permitir al usuario crear un estudiante mediante `input()` y luego imprimirlo.

---

## ✅ Criterios de evaluación
- Correcta implementación de **clases y objetos**
- Uso adecuado de **encapsulación, herencia y polimorfismo**
- Claridad y organización del código
- Comentarios explicativos

---

## 📖 Referencias
- Material de clase: *Clases y Objetos en Python*  
- Documentación oficial de Python: [https://docs.python.org/es/3/tutorial/classes.html](https://docs.python.org/es/3/tutorial/classes.html)
