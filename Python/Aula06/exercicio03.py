# Crie um programa que solicita ao usuário que insira três
# notas e, em seguida, calcule a média dessas notas
# usando uma função. A função deve receber as três
# notas como parâmetros e retornar a média. Por fim, o
# programa deve imprimir a média calculada.

def notas(nota01, nota02, nota03):
    calculo = (nota01+nota02+nota03)/3
    if calculo >= 7:
        return f"aprovado com media {calculo}"
    else:
        return f"reprovado com media {calculo}"

primeira_nota = float(input("Insera a primeira nota: "))
segunda_nota = float(input("Insira a segunda nota: "))
terceira_nota = float(input("Insira a terceira nota: "))

media = notas(primeira_nota, segunda_nota, terceira_nota)
print(media)