# Este programa demuestra los conceptos de POO en Python:
# - Herencia: La clase `Perro` y la clase `Gato` heredan de la clase `Animal`.
# - Encapsulación: Los atributos `__nombre` y `__edad` en la clase `Animal` son privados.
# - Polimorfismo: El método `hacer_sonido` se sobrescribe en las clases derivadas para proporcionar una implementación específica.

# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.__edad = edad  # Atributo encapsulado

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase")

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

# Otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau"

# Función principal
def main():
    # Crear una instancia de la clase Perro
    perro = Perro("Fido", 3, "Labrador")
    # Crear una instancia de la clase Gato
    gato = Gato("Whiskers", 2, "Blanco")

    # Imprimir los sonidos que hacen el perro y el gato
    print(f"El perro {perro.get_nombre()} de raza {perro.raza} dice: {perro.hacer_sonido()}")
    print(f"El gato {gato.get_nombre()} de color {gato.color} dice: {gato.hacer_sonido()}")

    # Mostrar la edad del perro y del gato usando los métodos getter
    print(f"El perro tiene {perro.get_edad()} años")
    print(f"El gato tiene {gato.get_edad()} años")

# Ejecutar la función principal
if __name__ == "__main__":
    main()