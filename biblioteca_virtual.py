from decoradores import registrar_operacion    
from libro import Libro
from usuario import Usuario, Estudiante, Profesor, Administrador
from prestamo import Prestamo
from HistorialPrestamos import HistorialPrestamos

class Singleton:
    _instance = None

    # Atributos de la Biblioteca Virtual
    def __init__(self):
        self.ListaUsuarios = []
        self.ListaLibros = []
        self.HistorialPrestamos = HistorialPrestamos() #Llamamos a la clase que incorpora una lista de prestamos
        
    #Metodo para crear una instancia de la clase Singleton para la Bilioteca Virtual
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Instancia creada")
        else:
            print("Instancia ya existe")
        return cls._instance
 
    #Metodos de la Biblioteca Virtual
    
    #Metodos de búsqueda para personas según dni, y para libros según código ISBN
        
    def BuscarUsuario(self, dni):
        for usuario in self.ListaUsuarios:
            if usuario.dni == dni:
                return usuario
        return None
    
    def BuscarLibro(self,ISBN):
        for libro in self.ListaLibros:
            if libro.ISBN == ISBN:
                return libro
        return None
    
   #Creación de usuarios según tipo 
   
    @registrar_operacion
    def AgregarEstudiante(self, nombre, apellido, email, dni, nro_legajo, carrera):
     estudiante = Estudiante(nombre, apellido, email,dni, nro_legajo, carrera)
     self.ListaUsuarios.append(estudiante)
   
    @registrar_operacion
    def AgregarProfesor(self, nombre, apellido, email, dni, departamento):
        profesor = Profesor(nombre, apellido, email, dni, departamento)
        self.ListaUsuarios.append(profesor)
        
    @registrar_operacion    
    def AgregarAdministrador(self, nombre, apellido, email, dni):
        administrador = Administrador(nombre, apellido, email, dni)
        self.ListaUsuarios.append(administrador)
   
   
   
 #Metodos para modificar, eliminar, ver lista de usuarios. Por 
    @registrar_operacion
    def ModificarUsuario(self, dni_buscado, nombre=None, apellido=None, email=None, dni=None, carrera = None, departamento = None):
        usuario = self.BuscarUsuario(dni_buscado)
        if usuario is not None:
            usuario.ModificarUsuario(nombre = nombre, apellido = apellido, email = email, dni = dni, carrera = carrera, departamento = departamento)
            print(f"Usuario modificado correctamente.")
            return True
        print(f"Usuario no encontrado.")
        return False
              
    @registrar_operacion
    def EliminarUsuario(self,dni_buscado):
        usuario = self.BuscarUsuario(dni_buscado)
        if usuario is not None:
            self.ListaUsuarios.remove(usuario)
            print(f"Usuario eliminado correctamente.")
            return True
        print(f"Usuario no encontrado.")
        return False
    
       
    def ListarUsuarios(self): #ver la lista de usuarios
       for usuario in self.ListaUsuarios:
              print(usuario)
       
   

    #PARA LOS LIBROS
    @registrar_operacion
    def AgregarLibro(self, titulo, autor, anio_publicacion, ISBN, cantidad_paginas, Genero, estado):
        nuevo_libro = self.Libro(titulo, autor, anio_publicacion, ISBN, cantidad_paginas, Genero, estado)
        self.ListaLibros.append(nuevo_libro)
     
    @registrar_operacion
    def ModificarLibro(self, ISBN_buscado, titulo=None, autor=None, anio_publicacion=None, ISBN=None, cantidad_paginas=None, Genero= None, estado=None):
        #Se modifica un libro existente (sus datos)
        libro = self.BuscarLibro(ISBN_buscado)
        if libro is not None:
            libro.modificarLibro(titulo=titulo, 
                                     autor=autor, 
                                     anio_publicacion=anio_publicacion,      
                                     ISBN=ISBN,
                                     cantidad_paginas=cantidad_paginas,
                                     Genero=Genero,
                                     estado=estado)
            return True
        print("Libro no encontrado")
        return False


    @registrar_operacion
    def EliminarLibro(self, ISBN):
        libro = self.BuscarLibro(ISBN)
        if libro is not None:
            self.ListaLibros.remove(libro)
            return True
        print("Libro no encontrado")
        return False

    def ListarLibros(self):
        #Se listan todos los libros
        for libro in self.ListaLibros:
            print(libro)
    
    
    #Con respecto a los prestamos, se registran los prestamos y devoluciones de libros, ademas de consultar los prestamos activos y el historial de prestamos.
    
    @registrar_operacion
    def RegistrarPrestamo(self, dni_usuario, ISBN_libro):
        
        usuario = self.BuscarUsuario(dni_usuario)
        libro = self.BuscarLibro(ISBN_libro)
        
        if usuario is None:
            print('Usuario no encontrado')
            return False
        
        if libro is None:
            print('Libro no encontrado')
            return False
             
        if libro.estado is False:
            print('Libro no disponible')
            return False 

        prestamo = Prestamo(usuario=usuario,libro=libro)
        
        self.HistorialPrestamos.Prestamos.append(prestamo)
        usuario.prestamos.append(prestamo)
        libro.estado = False

    def RegistrarDevolucion(self, ISBN):
        self.HistorialPrestamos.RegistrarDevolucion(ISBN)
    
    def ConsultarPrestamosActivos(self):
        self.HistorialPrestamos.ConsultarPrestamosActivos()

    def MostrarHistorialPrestamos(self):
        self.HistorialPrestamos.MostrarHistorial()
        
        
