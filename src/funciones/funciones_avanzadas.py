def numeros_pares(a: int, b: int, c: int, d: int, e: int) -> list[int]:
    numeros:int = [a,b,c,d,e]
    if numeros % 2 == 0:
        pares:int=numeros
    return pares
# print(numeros_pares(4,2,3,5,6))

def suma(a: int, b: int) -> int:
    return a+b
print(suma(34))

def login(user="",passw=""):
    return "bienvenido al sistema"
print(login(passw="11111",user="hola"))