soma = 0

for numero in range(3,501): # Do alcance de 3 a 501
    if numero % 3 == 0:
        print(numero)
        soma += numero # Operador de incremento x = x + 3

print("A soma dos multiplos de 3 até 500 é: ", soma)
    