print("Bem vindo a calculadora Geral para apenas duas variaveis INTEIRAS.")

# Declaração dos numeros a serem operados
num1 = input("digite o numero a ser operado: ")
num2 = input("digite outro numero a ser operado: ")

# Todas as operaçoes entre dois numeros
resSoma = int(num1) + int(num2)
resSubt = int(num1) - int(num2)
resMult = int(num1) * int(num2)
resDiv = int(num1) / int(num2)
resDivResto = int(num1) % int(num2)

# Print dos resultados
print("Soma:")
print(resSoma)
print("Subtração")
print(resSubt)
print("Multiplicação:")
print(resMult)
print("Divisão:")
print(resDiv)
print("Resto da divisão:")
print(resDivResto)