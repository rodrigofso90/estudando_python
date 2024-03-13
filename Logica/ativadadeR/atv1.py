# Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# Salário bruto
# Quanto pagou ao INSS.
# Quanto pagou ao sindicato.
# O salário líquido.

# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto : R$
# IR (11%) : R$
# INSS (8%) : R$
# Sindicato ( 5%) : R$
# Salário Liquido : R$

valor = float(input("Insira o valor por hora: "))
hora = int(input("Insira a quantidade de horas trabalhadas: "))


salario = hora * valor*30
imposto_renda = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liquido = salario - imposto_renda - inss - sindicato



print(f"O salario bruto é {salario}")
print(f"O valor do imposto de renda é {imposto_renda}")
print(f"O valor do inss é {inss}")
print(f"O valor pago ao sindicato é {sindicato}")
print(f"Salario liquido é {salario_liquido:.2f}")