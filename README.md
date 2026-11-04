## Trabajo Practico Final Programación Avanzada: Desarrollo de Biblioteca Virtual Universitaria

### Integrantes: Luciana Sol Parallela, Camila Belén Gonzalez,.

#### Descripción breve del trabajo:

Se ha desarrollado un sistema de Biblioteca Universitaria, que permite administrar usuarios, libros y préstamos. 
El sistema contempla distintos tipos de usuarios (Estudiante, Profesor y Administrador), gestión de préstamos y devoluciones, historial de préstamos y búsquedas de información. Además, se implementaron conceptos avanzados de Programación Orientada a Objetos como el patrón de diseño Singleton, también un decorador y una metaclase. 

## Instrucciones de uso

1. Clonar o descargar el repositorio.

2. Abrir el proyecto en Visual Studio Code.

3. Verificar que todos los archivos del proyecto se encuentren en la misma carpeta:

* `main.py`
* `biblioteca_virtual.py`
* `usuario.py`
* `libro.py`
* `prestamo.py`
* `HistorialPrestamos.py`
* `decoradores.py`
* `metaclase.py`

4. Ejecutar el archivo `main.py`.

5. Crear una instancia de la biblioteca virtual:

```python
biblioteca = Singleton()
```

6. Utilizar los métodos provistos por la clase para administrar el sistema:

* `AgregarEstudiante()`
* `AgregarProfesor()`
* `AgregarAdministrador()`
* `AgregarLibro()`
* `RegistrarPrestamo()`
* `RegistrarDevolucion()`
* `ConsultarPrestamosActivos()`
* `MostrarHistorialPrestamos()`

7. El sistema incorpora:

* Patrón Singleton para garantizar una única instancia de la biblioteca.
* Decorador `@registrar_operacion` para registrar operaciones importantes.
* Metaclase `MetaEntidad` para verificar la implementación del método `mostrar_info()`.

## Diagrama UML

El diagrama UML del sistema se encuentra en:


docs/Diagrama UML.drawi
