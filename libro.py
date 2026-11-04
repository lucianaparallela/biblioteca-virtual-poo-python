from metaclase import MetaEntidad

class Libro(metaclass=MetaEntidad): 
    def __init__(self, titulo, autor, anio_publicacion, ISBN, cantidad_paginas, Genero, estado=True): #Lo instanciamos como True porque cuando se crea un libro, este está disponible para prestar
        self.titulo = titulo 
        self.autor = autor
        self.anio_publicacion = anio_publicacion 
        self.ISBN = ISBN 
        self.cantidad_paginas = cantidad_paginas 
        self.Genero = Genero
        self.estado = estado #si el estado es true el libro esta disponible, si es false no esta disponible
  

    def mostrar_info(self): 
        return (
            f"Título: {self.titulo}, "
            f"Autor: {self.autor}, "
            f"Año de publicación: {self.anio_publicacion}, "
            f"ISBN: {self.ISBN}, "
            f"Cantidd de páginas: {self.cantidad_paginas}, "
            f"Género: {self.Genero}, "
            f"Estado: {'Disponible' if self.estado else 'No disponible'}"
        )
        
    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Año de publicación: {self.anio_publicacion} | ISBN: {self.ISBN} | Cantidad de páginas: {self.cantidad_paginas} | Género: {self.Genero} | Estado: {'Disponible' if self.estado else 'No disponible'}"

    def modificarLibro(self, titulo=None, autor=None, anio_publicacion=None, ISBN=None, cantidad_paginas=None, Genero=None, estado=None):
        if titulo is not None:
            self.titulo = titulo
        if autor is not None:
            self.autor = autor
        if anio_publicacion is not None:
            self.anio_publicacion = anio_publicacion
        if ISBN is not None:
            self.ISBN = ISBN
        if cantidad_paginas is not None:
            self.cantidad_paginas = cantidad_paginas
        if Genero is not None:
            self.Genero = Genero
        if estado is not None:
            self.estado = estado