
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero%3 != 0:
        continue
    else:
        print(numero)
        
# Otra solución
for i in range(10):
    if i % 3 == 0:
        print(i)