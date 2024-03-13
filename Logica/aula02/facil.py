

n1 = int(input("Digite: "))
n2 = int(input("Digite: "))
n3 = int(input("Digite: "))


if n1>n2 and n1>n3:
    maior = n1
    if n2>n3:
        meio = n2
        menor = n1
    else:
        menor = n2
        meio = n3

if n2>n1 and n2>n3:
    maior = n2
    if n1>n3:
        meio = n1
        menor = n3
    else:
        menor = n1
        meio = n3

if n3>n2 and n3>n1:
    maior = n3
    if n2>n1:
        meio = n2
        menor = n1
    else:
        menor = n2
        meio = n1


print(f"O maior numero é: {maior}, meio {meio}, menor {menor}")