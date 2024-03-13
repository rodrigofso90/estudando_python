# Crie uma calculadora com opções 1 - soma, 2 - multiplicação, 3- subtração, 4 - divisao e 5 - Sair.

# (ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora)
# utilize funções para cada operação, realizar os cáculos os cálculos.

# Dica:utilize de condicionais e laços de repetição para realizar esse exercício.

# A Operação deve ser realizada com argumentos apenas

def soma(num1, num2):
    return num1 + num2

def multiplicacao(num1, num2):
    return num1 * num2

def subtracao(num1, num2):
    return num1 - num2

def divisao(num1, num2):
    return num1 / num2


while True:
    valor_digitado = float(input("Digite opção desejada:\n 1 - Soma: \n 2 - Multiplicação: \n 3 - Subtração: \n 4 - Divisao: \n 5 - Sair \n"))
    if valor_digitado != 5:
        num1 = float(input("Insira o primeiro numero: "))
        num2 = float(input("Insira o segundo numero: "))

    if valor_digitado == 1:
        print(soma(num1, num2))
    elif valor_digitado == 2:
        print(multiplicacao(num1, num2))
    elif valor_digitado == 3:
        print(subtracao(num1, num2))
    elif valor_digitado == 4:
        print(divisao(num1, num2))
    else:
        break

