def registrar_operacion(funcion):

    def wrapper(*args, **kwargs):

        print(
            f"[REGISTRO] Iniciando operación: {funcion.__name__}"
        )

        resultado = funcion(*args, **kwargs)

        print(
            f"[REGISTRO] Operación finalizada: {funcion.__name__}"
        )
        return resultado 
    
    return wrapper 

