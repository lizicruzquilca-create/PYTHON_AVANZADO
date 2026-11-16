### 8. Closure (Clausura) 
# Escribe una función externa llamada crear_validador_limite(limite_maximo: int) que retorne una función 
# interior. Esta función interior debe recibir un número y retornar True si es menor o igual al 
# limite_maximo, o False si lo supera. Pon a prueba tu closure creando un validador con límite 100. 
def crear_validador_limite(limite_maximo: int):
    def validar(numero: int | float) -> bool:
        return numero <= limite_maximo
    return validar

# Prueba creando un validador con límite 100
validar_hasta_100 = crear_validador_limite(100)

print(validar_hasta_100(85))   # Salida: True
print(validar_hasta_100(120))  # Salida: False
