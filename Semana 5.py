# Programa para calcular el área de un triángulo
# Función para calcular el área del triángulo
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
# Datos de entrada del usuario
base_triangulo = float(input("Ingresa la base del triángulo: "))
altura_triangulo = float(input("Ingresa la altura del triángulo: "))
# Calcular el área del triángulo
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
# Mostrar el resultado
print(f"El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es {area_triangulo}")