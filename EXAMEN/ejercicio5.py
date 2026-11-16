### 5. Empaquetado Nominal (**kwargs) 
# Diseña una función llamada generar_perfil_usuario(**kwargs) que reciba datos arbitrarios 
# en formato clave-valor (como nombre, edad, país, profesión) y devuelva una cadena de 
# texto descriptiva que recorra el diccionario armado e imprima cada característica del usuario. 

def generar_perfil_usuario(**kwargs: Any) -> str:
    if not kwargs:
        return "Perfil sin datos registrados."

    lineas_perfil: list[str] = ["Perfil de Usuario"]

    for clave, valor in kwargs.items():
        clave_formateada: str = clave.capitalize()
        lineas_perfil.append(f"- {clave_formateada}: {valor}")

    resultado: str = "\n".join(lineas_perfil)
    return resultado


# Pruebas con distinta cantidad de datos nominales
perfil_1: str = generar_perfil_usuario(
    nombre="Ana", edad=28, pais="Perú", profesion="Ingeniera"
)
print(perfil_1)

print()  # Línea en blanco para separar las salidas

perfil_2: str = generar_perfil_usuario(
    usuario="carlos_dev", lenguaje="Python", activo=True
)
print(perfil_2)
