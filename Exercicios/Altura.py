alturas = []
valor = 0

for i in range(15):
    valor = input(f"Digite a altura {i + 1}: ")
    alturas.append(valor)

print(f"As alturas são: ",alturas)

maior_altura = max(alturas)
menor_altura = min(alturas)

print(f"Maior altura: ", maior_altura)
print(f"Menor altura: ", menor_altura)