'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''

acum = 0
contador = 0
for i in range(10):
    n = int(input("Introduce un número: "))
    acum += n
    contador += 1
prom = acum / contador
print(f"El promedio de los números es: {prom}")
