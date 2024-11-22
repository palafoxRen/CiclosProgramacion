'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''

import random
numsec = random.randint(1, 100)
max = 10
print("Tienes 10 intentos para adivinar un número entre 1 y 100.")
intentos = 0
while intentos < max:
    intento = int(input("Introduce tu número: "))
    intentos += 1
    if intento < numsec:
        print("El número es mayor. Intentos restantes:", max - intentos)
    elif intento > numsec:
        print("El número es menor. Intentos restantes:", max - intentos)
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
if intentos == max and intento != numsec:
    print(f"No adivinaste. El número secreto era {numsec}.")