#Desarrollar habilidades prácticas en la Programación Tradicional y la Programación Orientada a
# Objetos (POO) mediante
# la implementación de un programa en Python
# para determinar el promedio semanal del clima.
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

if name == "_main_":
    main()