#TIENDA ONLINE
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f'Producto: {self.nombre}, Precio: ${self.precio}'
class CarritoCompras:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f'Producto añadido: {producto}')
    def mostrar_carrito(self):
        for producto in self.productos:
            print(producto)
    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)
        return f'Total a pagar: ${total}'
# Ejemplo de uso
producto1 = Producto("Laptop", 1200)
producto2 = Producto("Mouse", 20)
carrito = CarritoCompras()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.mostrar_carrito()
print(carrito.calcular_total())
#
#
#SITEMA DE GESTION EMPLEADOS
class Empleado:
    def __init__(self, nombre, id_empleado, puesto):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.puesto = puesto
    def __str__(self):
        return f'Empleado: {self.nombre}, ID: {self.id_empleado}, Puesto: {self.puesto}'
class Empresa:
    def __init__(self):
        self.empleados = []
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f'Empleado añadido: {empleado}')
    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)
# Ejemplo de uso
empleado1 = Empleado("Maria Gomez", 1, "Ingeniera de Software")
empleado2 = Empleado("Carlos Diaz", 2, "Analista de Datos")
empresa = Empresa()
empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)
empresa.mostrar_empleados()