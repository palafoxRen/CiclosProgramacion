'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''

def limites():
    while True:
        liminf = int(input("Introduce el límite inferior del intervalo: "))
        limsup = int(input("Introduce el límite superior del intervalo: "))
        if liminf < limsup:
            return liminf, limsup
        else:
            print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")
liminf, limsup = limites()
sumaintervalo = 0
fueraintervalo = 0
igualimite = False
print("Introduce números (0 para terminar):")
while True:
    n = int(input())
    if n == 0:
        break
    if liminf < n < limsup:
        sumaintervalo += n
    else:
        fueraintervalo += 1
    if n == liminf or n == limsup:
        igualimite = True
print(f"Suma de los números dentro del intervalo: {sumaintervalo}")
print(f"Números fuera del intervalo: {fueraintervalo}")
if igualimite:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")