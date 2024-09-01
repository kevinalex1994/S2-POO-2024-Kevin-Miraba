class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    # Métodos para obtener y establecer los atributos
    def obtener_id(self):
        return self.id_producto
    def obtener_nombre(self):
        return self.nombre
    def establecer_nombre(self, nombre):
        self.nombre = nombre
    def obtener_cantidad(self):
        return self.cantidad
    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad
    def obtener_precio(self):
        return self.precio
    def establecer_precio(self, precio):
        self.precio = precio
    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}'
class Inventario:
    def __init__(self):
        self.productos = {}
    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)
        else:
            print("Producto no encontrado.")
    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.obtener_nombre().lower() == nombre.lower()]
        return resultados
    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(producto)
    def guardar_en_archivo(self, filename):
        with open(filename, 'w') as file:
            for producto in self.productos.values():
                file.write(f'{producto.obtener_id()},{producto.obtener_nombre()},{producto.obtener_cantidad()},{producto.obtener_precio()}\n')
    def cargar_desde_archivo(self, filename):
        try:
            with open(filename, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.añadir_producto(producto)
        except FileNotFoundError:
            print(f"El archivo {filename} no existe.")
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo('inventario.txt')
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == '2':
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = int(input("Ingrese nueva cantidad (o presione Enter para mantener): ") or 0)
            precio = float(input("Ingrese nuevo precio (o presione Enter para mantener): ") or 0.0)
            inventario.actualizar_producto(id_producto, cantidad or None, precio or None)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")
        elif opcion == '5':
            inventario.mostrar_todos_los_productos()
        elif opcion == '6':
            inventario.guardar_en_archivo('inventario.txt')
            print("Inventario guardado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == '__main__':
    menu()