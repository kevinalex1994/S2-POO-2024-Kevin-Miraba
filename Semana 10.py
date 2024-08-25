import os
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    # Getters
    def get_id_producto(self):
        return self.id_producto
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio
    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio
    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'
class Inventario:
    def __init__(self, filename='inventario.txt'):
        self.filename = filename
        self.productos = []
        self.cargar_inventario()
    def cargar_inventario(self):
        """Load the inventory from a file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    for line in file:
                        id_producto, nombre, cantidad, precio = line.strip().split(',')
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                print("Inventario cargado exitosamente.")
            except FileNotFoundError:
                print(f"Error: No se pudo encontrar el archivo {self.filename}.")
            except PermissionError:
                print(f"Error: No se tiene permiso para leer el archivo {self.filename}.")
            except Exception as e:
                print(f"Error inesperado al cargar el inventario: {e}")
        else:
            print(f"El archivo {self.filename} no existe. Se creará uno nuevo al añadir productos.")
    def guardar_inventario(self):
        """Save the inventory to a file."""
        try:
            with open(self.filename, 'w') as file:
                for producto in self.productos:
                    file.write(f'{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Error: No se tiene permiso para escribir en el archivo {self.filename}.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")
    def añadir_producto(self, producto):
        if not any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido exitosamente.")
        else:
            print("Error: El ID del producto ya existe.")
    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")
    def buscar_producto_por_nombre(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")
    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")
def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
def main():
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventarios...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
if __name__ == "__main__":
    main()