### 6. Funciones Anónimas (lambda) 
# Crea una función anónima (lambda) asignada a una variable llamada es_par que reciba un número entero 
# y devuelva True si es par y False en caso contrario. Pruébala pasando un número par y uno impar. 

def calcular_potencia(base: float, exponente: float) -> float:

    if exponente < 0:
        raise ValueError("El exponente no debe ser negativo")

    return base ** exponente


# Prueba
print("Resultado:", calcular_potencia(2.0, 3.0))