'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''

mes = 1
pago = 10
total = 0
while mes <= 20:
    print(f"Mes {mes}: {pago} euros")
    total += pago
    pago *= 2 
    mes += 1
print(f"\nEl total pagado después de 20 meses es: {total} euros")