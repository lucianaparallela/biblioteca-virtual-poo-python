class MetaEntidad(type): 

    def __new__(cls, nombre, bases, atributos): #Atributos: dicc donde se guardan lo que escribi dentro de la clase

       tiene_mostrar_info = "mostrar_info" in atributos 

       #Se verifica si alguna clase padre tiene mostrar_info()
       #Esto permite que clases hijas (Estudiante, profesor y Admin) puedan heredar el
       #método desde Usurario sin tener que redefinirlo
       
       hereda_mostrar_info = any(
              hasattr(base, "mostrar_info") for base in bases  
       )


       #Si la clase no tiene mostrar_info() y tampoco lo hereda de una que lo tenga
       #Se lanza el error

       if not tiene_mostrar_info and not hereda_mostrar_info: 
              
            raise TypeError(f"La clase {nombre} debe implementar el método mostrar_info()"
            )
       
       return super().__new__(
           cls, 
           nombre, 
           bases,
           atributos
       )