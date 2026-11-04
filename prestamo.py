from datetime import date, timedelta
from metaclase import MetaEntidad


class Prestamo(metaclass=MetaEntidad): 
    
    def __init__(self, usuario, libro,estado=True):
        self.usuario = usuario 
        self.libro = libro 
        
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.fecha_devolucion_estimada = self.fecha_prestamo + timedelta(days=30) #Los libros se prestan por 30 dias desde la fecha de prestamo


    def finalizar(self): 
        self.estado = False
        self.libro.estado = True
        self.fecha_devolucion = date.today()

    def esta_activo(self): 
        return self.estado == True 
    
    def mostrar_info(self): 
        return ( 
            f"\nUsuario: {self.usuario.nombre} {self.usuario.apellido}, "
            f"\nLibro: {self.libro.titulo}, "
            f"\nFecha de devolución correspondiente: {self.fecha_devolucion_estimada}, "
            f"\nFecha de préstamo: {self.fecha_prestamo}, "
            f"\nEstado: {'Activo' if self.estado else 'Finalizado'}, "
        )

def __str__(self):
    return (
        f"Usuario: {self.usuario.nombre} {self.usuario.apellido}\n"
        f"Libro: {self.libro.titulo}\n"
        f"Fecha préstamo: {self.fecha_prestamo}\n"
        f"Fecha de devolución correspondiente: {self.fecha_devolucion_estimada}\n"
        f"Estado: {'Activo' if self.estado else 'Finalizado'}"
    )
    
