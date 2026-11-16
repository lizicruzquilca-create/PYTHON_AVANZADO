### 2. Parámetros Nominales y por Defecto 
# Crea una función llamada calcular_precio_final que calcule el precio de un producto aplicando 
# un impuesto y un descuento opcional. 
# ● Parámetros por defecto: impuesto = 0.18 (18%) y descuento = 0.0. 
# ● Utiliza argumentos nominales en su llamada para aplicar solo un 
# descuento del 0.05 (5%) manteniendo el impuesto por defecto. 

def calcular_precio_final(precio_base: int | float, impuesto: float = 0.18, descuento: float = 0.0,) -> float:
    precio_con_impuesto = precio_base * (1 + impuesto)
    precio_final = precio_con_impuesto * (1 - descuento)
    return float (precio_final)

total = calcular_precio_final(100, descuento=0.05)
print("El precio final es:", total)
