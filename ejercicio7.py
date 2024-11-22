'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''

def vocal(letra):
    return letra.lower() in 'aeiou'
while True:
    letra = input("Introduce un carácter: (introduce un espacio y enter para terminar).")
    if letra == ' ':
        break
    if vocal(letra):
        print("VOCAL")
    else:
        print("NO VOCAL")