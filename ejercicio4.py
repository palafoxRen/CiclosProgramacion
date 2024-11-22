'''
Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''

num = [1, 2, 3, 4, 5]
for num in num:
    print(f"Tabla de multiplicar del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()         