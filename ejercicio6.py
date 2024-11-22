'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''

cant = int(input("¿Cuántos números quieres introducir? "))
mayor = 0
menor = 0
igual = 0
for i in range(cant):
    numero = int(input("Introduce un número: "))
    if numero > 0:
        mayor += 1
    elif numero < 0:
        menor += 1
    else:
        igual += 1
print(f"Números mayores que 0: {mayor}")
print(f"Números menores que 0: {menor}")
print(f"Números iguales a 0: {igual}")