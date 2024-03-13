nota01 = float(input("Insira a primeira nota: "))
nota02 = float(input("Insira a segunda nota: "))
nota03 = float(input("Insira a terceira nota: "))

media = (nota01+nota02+nota03)/3

if media >= 7:
    print(f"Aluno foi aprovado com a nota {media:.2f}")
else:
    print(f"Aluno foi reprovado com a nota {media:.2f}")
     