pocet = 0
suma = 0
for cena in 1.75, 2.20, 1.03, 4.00, 3.50, 2.90, 1.89:
    suma = suma + cena
    pocet = pocet + 1
print('nakupl si', pocet, 'ploziek')
print('za', suma, 'euro')
print('priemerna cena bola', round(suma / pocet,0), 'euro')