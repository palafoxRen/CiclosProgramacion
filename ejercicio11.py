'''
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
'''

import math
n = int(input("Introduce un número: "))
def primo(num):
    if num <= 1:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True
if primo(n):
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")