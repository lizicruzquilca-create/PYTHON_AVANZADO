#crear una funcion que me permita ingresar nombre, apellido y me retorne un mensaje con ambos datos
def creador(nombre:srt):
    def apellido(ap:srt):
        return f"tu nombre es: {nombre} y tu apellido es {ap}"
    return apellido
alumno1=creador("david") # def apellido(ap):return
print(alumno("goliat"))


## Usando closure crear un función multiplicador que resiva por parametro el factor que devuelva una función que permita multiplicar cualquier numero por el factor
def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

por_tres = multiplicador(3)
por_cinco = multiplicador(10)

print(por_tres(5))    # Salida: 15
print(por_tres(8))    # Salida: 24
print(por_cinco(4))    # Salida: 20