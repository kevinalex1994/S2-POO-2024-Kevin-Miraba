#El código define una clase Archivo en Python que simula la apertura y cierre de un archivo usando un constructor __init__
#para inicializar el objeto y abrir el archivo, y un destructor __del__ para cerrar el archivo cuando el objeto es eliminado.
#El método escribir permite escribir contenido en el archivo si está abierto. Comentarios y mensajes informativos en el código explican y confirman las operaciones, demostrando el uso adecuado de constructores y destructores en Python para inicializar y limpiar recursos.
class Archivo:
    def __init__(self, nombre):
        """Constructor que inicializa el objeto Archivo con el nombre del archivo."""
        self.nombre = nombre
        self.archivo = None
        try:
            # Intentamos abrir el archivo
            self.archivo = open(nombre, 'w')
            print(f"Archivo '{self.nombre}' ha sido abierto para escritura.")
        except Exception as e:
            print(f"No se pudo abrir el archivo '{self.nombre}': {e}")
    def escribir(self, contenido):
        """Método para escribir contenido en el archivo."""
        if self.archivo:
            self.archivo.write(contenido)
            print(f"Se ha escrito en el archivo '{self.nombre}'.")
def __del__(self):
        """Destructor que cierra el archivo si está abierto."""
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' ha sido cerrado.")
# Uso de la clase Archivo
archivo1 = Archivo("mi_archivo.txt")
archivo1.escribir("Este es el contenido del archivo.\n")
# Forzar la eliminación del objeto para llamar al destructor
del archivo1
# Crear otro objeto de la clase Archivo
archivo2 = Archivo("otro_archivo.txt")
archivo2.escribir("Contenido del segundo archivo.\n")
# No es necesario llamar explícitamente a 'del', el recolector de basura de Python se encargará de ello