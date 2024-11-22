'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
print(f"Números pares entre {num1} y {num2}:")
for x in range(num1, num2 + 1):
    if x % 2 == 0:
        print (x)