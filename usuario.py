from metaclase import MetaEntidad

class Usuario(metaclass=MetaEntidad):
   def __init__(self, nombre, apellido, email, dni):
       self.nombre = nombre
       self.apellido = apellido
       self.dni = dni
       self.email = email
       self.prestamos = []

   def mostrar_info(self):
       return (
           f"Nombre: {self.nombre}, "
           f"Apellido: {self.apellido}, "
           f"Email: {self.email}, "
           f"DNI: {self.dni} "  
        )

   def __str__(self):
         return f"Usuario: {self.nombre} {self.apellido} | Email: {self.email} | DNI: {self.dni}"

   def ModificarUsuario(self, nombre=None, apellido=None, email=None, dni=None):
        if nombre is not None:
            self.nombre = nombre
        if apellido is not None:
            self.apellido = apellido
        if email is not None:
            self.email = email
        if dni is not None:
            self.dni = dni

class Estudiante(Usuario): 
    def __init__(self, nombre, apellido, email, dni, nro_legajo, carrera): 
        super().__init__(nombre, apellido, email, dni)
        self.nro_legajo = nro_legajo 
        self.carrera = carrera 

    def mostrar_info(self): 
        return ( 
           super().mostrar_info() 
           + f"\nNumero de legajo: {self.nro_legajo}"
           + f"\nCarrera: {self.carrera}"
        )   
    
    #AGREGO ESTO PARA QUE SE PUEDA MODIFICAR LA CARRERA DEL ESTUDIANTE, ADEMAS DE LOS DATOS DEL USUARIO
    def ModificarUsuario(self, nombre=None, apellido=None, email=None, dni=None, carrera=None):
        super().ModificarUsuario(nombre, apellido, email,dni)
        if carrera is not None:
            self.carrera = carrera

    
class Profesor(Usuario): 
    def __init__(self, nombre, apellido, email, dni, departamento): 
        super().__init__(nombre, apellido, email, dni)
        if departamento is not None: 
            self.departamento = departamento 

    def mostrar_info(self): 
        return ( 
            super().mostrar_info()
            + f"\nDepartamento: {self.departamento}"
        )
    
    #AGREGO ESTO PARA QUE SE PUEDA MODIFICAR EL DEPARTAMENTO DEL PROFESOR, ADEMAS DE LOS DATOS DEL USUARIO
    def ModificarUsuario(self, nombre=None, apellido=None, email=None, departamento=None):
        super().ModificarUsuario(nombre, apellido, email)
        self.departamento = departamento

    
class Administrador(Usuario): 
    def __init__(self, nombre, apellido, email, dni): 
        super().__init__(nombre, apellido, email, dni)
    
    def administrar_biblioteca(self): 
        return "El/La administrador/a está gestionando la biblioteca"
    
    def ModificarUsuario(self, nombre=None, apellido=None, email=None, dni=None):
        return super().ModificarUsuario(nombre, apellido, email, dni)