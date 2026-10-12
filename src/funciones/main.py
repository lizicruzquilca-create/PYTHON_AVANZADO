# crear un programa que me permita mostrar mensajes personalizadoss, 
# crear una funcion similar a la funcion print de python.

def numeros_pares(a: int, b: int, c: int, d: int, e: int) -> list[int]:
    numeros:int = [a,b,c,d,e]
    if numeros % 2 == 0:
        pares:int=numeros
    return pares


otra manera
def numeros_pares(a: int, b: int, c: int, d: int, e: int) -> list[int]:
    numeros:int = [a,b,c,d,e]
    if numeros % 2 == 0:
        pares:int=numeros
    return pares
print(numeros_pares(4,2,3,5,6))