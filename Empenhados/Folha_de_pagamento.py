valor_da_hora = float
hora_trabalhada = float

salario_bruto = float
salario_descontado_IR = float
salario_liquido = float
salario_posDescontodoInss = float

desconto = float(0)

Valor_da_hora = input ("Qual o valor da sua hora: ")
hora_trabalhada = input ("Horas trabalhadas: ")

salario_bruto = float(Valor_da_hora) * float(hora_trabalhada)
fgts = salario_bruto * 0.11 
salario_posDescontodoInss = salario_bruto * 0.10

print("")

if salario_bruto <= 900:
    
    print(f'Salário bruto: ', salario_bruto)
    print(f"(-) INSS: ", salario_posDescontodoInss)
    print(f'O salario liquido: ', salario_liquido) # Isento do Imposto de renda
    sum_descontos = desconto + fgts
    print(f"Total de descontos: ", sum_descontos)

elif salario_bruto <= 1500:

    print(f'Salário bruto: ', salario_bruto)
    salario_descontado_IR = salario_bruto * 0.05 # desconto de 5%
    print(f'(-) IR: ', salario_descontado_IR ) 
    print(f"(-) INSS: ", salario_posDescontodoInss)
    desconto = salario_posDescontodoInss + salario_descontado_IR
    
    sum_descontos = desconto + fgts
    print(f"Total de descontos: ", sum_descontos)

    salario_liquido = salario_bruto - desconto
    print(f'O salario liquido é: ', salario_liquido)

elif salario_bruto <= 2500:

    print(f'Salário bruto: ', salario_bruto)
    salario_descontado_IR = salario_bruto * 0.10 # desconto de 10%
    print(f'(-) IR: ', salario_descontado_IR ) 
    print(f"(-) INSS: ", salario_posDescontodoInss)
    desconto = salario_posDescontodoInss + salario_descontado_IR
    
    sum_descontos = desconto + fgts
    print(f"Total de descontos: ", sum_descontos)

    salario_liquido = salario_bruto - desconto
    print(f'O salario liquido é: ', salario_liquido)

elif salario_bruto > 2500:

    print(f'Salário bruto: ', salario_bruto)
    salario_descontado_IR = salario_bruto * 0.20 # desconto de 20%
    print(f'(-) IR: ', salario_descontado_IR ) 
    print(f"(-) INSS: ", salario_posDescontodoInss)
    desconto = salario_posDescontodoInss + salario_descontado_IR
    
    sum_descontos = desconto + fgts
    print(f"Total de descontos: ", sum_descontos)

    salario_liquido = salario_bruto - desconto
    print(f'O salario liquido é: ', salario_liquido)

print("")
print("Encerrando...")