'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''

def primo(num):
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
cant = int(input("Introduce la cantidad de números primos que quieres mostrar: "))
primos = 0
numero = 2
print("Los primeros", cant, "números primos son:")
while primos < cant:
    if primo(numero):
        print(numero)
        primos += 1
    numero += 1