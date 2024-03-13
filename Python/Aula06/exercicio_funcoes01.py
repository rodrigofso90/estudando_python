# Crie uma função que recebe 2 parametros
# essa função deve realizar o produto/multiplicaçao dos dois paramentros.
# Retorne esse valor e imprima no console.
# ex: def soma(numeoro_1, numero_2)


def multiplicacao(num1, num2):
    return num1 * num2

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))

calculo = multiplicacao(num1, num2)

print(calculo)