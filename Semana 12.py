class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (titulo, autor)  # Tupla para título y autor
        self.categoria = categoria
        self.isbn = isbn
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f'Libro "{libro.detalles[0]}" añadido.')
        else:
            print("El libro ya existe en la biblioteca.")
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f'Libro "{eliminado.detalles[0]}" eliminado.')
        else:
            print("El libro no se encuentra en la biblioteca.")
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f'Usuario "{usuario.nombre}" registrado.')
        else:
            print("El ID de usuario ya está registrado.")
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f'Usuario "{usuario.nombre}" dado de baja.')
        else:
            print("El usuario no está registrado.")
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f'Libro "{libro.detalles[0]}" prestado a {usuario.nombre}.')
        else:
            print("El usuario o el libro no existen.")
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f'Libro "{libro.detalles[0]}" devuelto por {usuario.nombre}.')
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("El usuario no está registrado.")
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and libro.detalles[0] == valor) or \
                    (criterio == "autor" and libro.detalles[1] == valor) or \
                    (criterio == "categoria" and libro.categoria == valor):
                resultados.append(libro)
        if resultados:
            for libro in resultados:
                print(f'Encontrado: {libro.detalles[0]} por {libro.detalles[1]} (ISBN: {libro.isbn})')
        else:
            print("No se encontraron libros que coincidan con el criterio.")
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f'Libros prestados a {usuario.nombre}:')
                for libro in usuario.libros_prestados:
                    print(f'- {libro.detalles[0]} por {libro.detalles[1]}')
            else:
                print(f'{usuario.nombre} no tiene libros prestados.')
        else:
            print("El usuario no está registrado.")
# Pruebas del sistema
# Crear biblioteca
biblioteca = Biblioteca()
# Crear libros
libro1 = Libro("1984", "George Orwell", "Ficción", "1234567890")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", "0987654321")
# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
# Crear usuario
usuario1 = Usuario("Juan Pérez", "001")
# Registrar usuario
biblioteca.registrar_usuario(usuario1)
# Prestar libro
biblioteca.prestar_libro("001", "1234567890")
# Devolver libro
biblioteca.devolver_libro("001", "1234567890")
# Buscar libro
biblioteca.buscar_libro("titulo", "1984")
# Listar libros prestados
biblioteca.listar_libros_prestados("001")