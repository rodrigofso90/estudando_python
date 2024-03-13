dicionario_alunos = dict()

while True:
    nome = input("digite o nome do aluno ou -1 para sair: ")
    if nome == "-1":
        break
    else:
        nota_matematica = float(input("Digite a nota de Matemática: "))
        nota_ciencias = float(input("Digite a nota de Ciências: "))
        nota_historia = float(input("Digite a nota de História: "))
        tupla_notas = (nota_matematica, nota_ciencias, nota_historia)
        dicionario_alunos[nome] = tupla_notas

print(dicionario_alunos)