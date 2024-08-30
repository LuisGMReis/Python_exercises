#3) Desenvolver um algoritmo que leia um número não determinado de valores 
#e calcule e escreva a média aritmética dos valores lidos, 
#a quantidade de valores positivos, a quantidade de valores

lista = []

media = 0
soma = 0
valor = None

while valor != 0:
    valor = int(input(f"Digite números e 0 para encerrar: "))
    soma += valor
    
    if valor != 0:
        lista.append(valor)

media = soma / len(lista)

print(f"Esses são os valores: ",lista)
print(f"Essa é média dessses valores: ",media)