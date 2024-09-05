Valor_da_hora = float(input("Qual o valor da sua hora: "))
hora_trabalhada = float(input("Horas trabalhadas: "))

salario_bruto = Valor_da_hora * hora_trabalhada
fgts = salario_bruto * 0.11 
salario_posDescontodoInss = salario_bruto * 0.10

desconto_IR = (
    salario_bruto * 0.05 if salario_bruto <= 1500
    else salario_bruto * 0.10 if salario_bruto >= 2500
    else salario_bruto * 0.20
)

desconto_total = salario_posDescontodoInss + desconto_IR
salario_liquido = salario_bruto - desconto_total

print()
print(f'Salário bruto: {salario_bruto}')
print(f'(-) INSS: {salario_posDescontodoInss}')
print(f'(-) IR: {desconto_IR}')
print(f'Total de descontos: {desconto_total}')
print(f'Salário líquido: {salario_liquido}')
print()
print("Encerrando...")
