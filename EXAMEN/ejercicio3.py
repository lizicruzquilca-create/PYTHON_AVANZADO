### 3. Type-hints (Anotaciones de tipo) 
# Diseña una función llamada obtener_promedio que reciba una lista de números enteros (list[int]) 
# y retorne un número flotante (float) que represente el promedio de los valores. 
# Incluye las anotaciones de tipo estrictas vistas en el apunte. 


def obtener_promedio(numeros: list[int]) -> float:
    if not numeros:
        return 0.0
    suma_total: int = sum(numeros)
    cantidad: int = len(numeros)
    promedio: float = suma_total / cantidad
    return promedio

notas: list[int] = [15, 18, 12, 20]
resultado: float = obtener_promedio(notas)
print("El promedio es:", resultado)
