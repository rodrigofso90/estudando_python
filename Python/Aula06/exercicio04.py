# Crie um programa que define uma função
# calcular_area_retangulo que recebe dois parâmetros,
# comprimento e largura de um retângulo, e retorna a
# área desse retângulo. 

# Em seguida, o programa deve
# solicitar ao usuário que insira o comprimento e a
# largura e imprimir a área calculada.

# formula: A = b x h


def calcular_area_retangulo(comprimento, largura):
    area = comprimento * largura
    return area

base = float(input("Insira o comprimento do retangulo: "))
altura = float(input("Insira a largura do retangulo: "))

area = calcular_area_retangulo(base, altura)

print(f"A área do retangulo é {area}")