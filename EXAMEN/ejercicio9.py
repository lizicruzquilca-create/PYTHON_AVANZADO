### 9. Programación Funcional (map()) 
# Dada una lista de precios en dólares: precios: list[float] = [10.5, 20.0, 50.0, 5.99], 
# utiliza la función integrada map() combinada con una función lambda para incrementar todos los precios 
# en un 10% (multiplicarlos por 1.10). Recuerda envolver el resultado en list() para visualizarlo. 
precios: list[float] = [10.5, 20.0, 50.0, 5.99]

precios_incrementados = list(map(lambda p: round(p * 1.10, 2), precios))
print(precios_incrementados)  # Salida: [11.55, 22.0, 55.0, 6.59]

precios: list[float] = [10.5, 20.0, 50.0, 5.99]

# Incrementar los precios en un 10%
precios_actualizados = list(
    map(lambda precio: precio * 1.10, precios)
)

print("Precios actualizados:", precios_actualizados)