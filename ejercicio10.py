'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''

b = float(input("Introduce la base (número real): "))
exp = int(input("Introduce el exponente (entero positivo): "))
r = 1
for x in range(exp):
    r *= b
print(f"El resultado de {b} elevado a {exp} es: {r}")