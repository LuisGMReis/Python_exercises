print("Bem vindo a calculadora Geral 2.0 para apenas duas variaveis INTEIRAS.")

sair = 0

while sair != 6:
    num1 = input("Digite o numero a ser operado: ")
    num2 = input("Digite outro numero a ser operado: ")

    #tres aspas pra ficar cada print em uma linha

    escolha = int(input("""1 para soma,
2 para subtração,
3 para multiplicação,
4 para divisão,
5 se quiser saber o resto da divisão,
e 6 pra sair: """))


    match escolha:
        case 1:
            resSoma = int(num1) + int(num2)
            print("Soma:")
            print(resSoma)
        case 2:
            resSubt = int(num1) - int(num2)
            print("Subtração")
            print(resSubt)
        case 3:
            resMult = int(num1) * int(num2)
            print("Multiplicação:")
            print(resMult)
        case 4:
            resDiv = int(num1) / int(num2)
            print("Divisão:")
            print(resDiv)
        case 5:
            resDivResto = int(num1) % int(num2)
            print("Resto da divisão:")
            print(resDivResto)
        case 6:
            sair = 6
        case _:
            print("opção invalida")