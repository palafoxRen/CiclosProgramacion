'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''

n = int(input("Introduce un número entero: "))
binario = ""
num = n
while num > 0:
    resto = num % 2
    binario = str(resto) + binario
    num = num // 2
print(f"El número {n} en binario es: {binario}")