# Faça um programa que solicite ao usuario a matricula doaluno e a nota associada a esta matricula.
# o programa deve solicitar as notas até o usuario digitar -1 para a matricula

# ao final do programa, imprima o dicionario

# dicionario = dict()

# dicionario['801'] = 9.0
# #dicionario = {'801':9.0}

# dicionario['903'] = 7.0




aluno_nota = dict()

while True:
    
    matricula = input("Digite o numero de matricula:")
    if matricula == "-1":
        break
    nota = float(input("Digite a nota: "))
    aluno_nota[matricula] = nota

print(aluno_nota)