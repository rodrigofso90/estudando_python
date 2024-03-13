# Crie um programa que, utilizando um loop for, encontre o primeiro número na sequência de 1 a 50 que seja

# inicio = int(input("Digite o número de inicio: "))
# fim = int(input("Digite o número final: "))

# for item in range(inicio, fim+1):
#     if item % 6 == 0:
#         break
#     print(item)


# _____________________________________________________________________________________________________


# Utilize um loop for para imprimir os números de 1 a 20, pulando os múltiplos de 3.

for item in range(1,21):
    if item % 3 == 0:
        continue
    print(item)