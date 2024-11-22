'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''

total = 0
mensual = []
for mes in range(1, 13):
    cantidad = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))
    total += cantidad
    mensual.append(total)
for mes, ahorro in enumerate(mensual, start=1):
    print(f"Mes {mes}: {ahorro:.2f}")
print(f"\nEl ahorro total al final del año es: {total:.2f}")