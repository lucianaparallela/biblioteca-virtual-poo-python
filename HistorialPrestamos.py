#Creamos una clase HistorialPrestamos para almacenar los prestamos realizados en la biblioteca virtual
#El objetivo fue agregar un caso de composicion. 
from decoradores import registrar_operacion  
from prestamo import Prestamo

class HistorialPrestamos:
    
    def __init__(self):
        self.Prestamos = []
        
    def MostrarHistorial(self):
        for prestamo in self.Prestamos:
            print(prestamo.mostrar_info())
        
    def ConsultarPrestamosActivos(self):
        #Se consultan los prestamos que estan activos
        for prestamo in self.Prestamos:
            if prestamo.estado:
                print(prestamo.mostrar_info())
                
    @registrar_operacion
    def RegistrarDevolucion(self, ISBN):
        for prestamo in self.Prestamos:

            if (prestamo.libro.ISBN == ISBN and prestamo.estado):
                prestamo.finalizar()
                return True

        return False