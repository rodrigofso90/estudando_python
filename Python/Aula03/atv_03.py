#crie uma lista vazia
#solicite ao usuário que digite 3 notas e inclua essa notas na lista
#calcule a soma desta nostas
#calcule a média das notas


nota01 = float(input('Insira a primeira nota: '))
nota02 = float(input('Insira a segunda nota: '))
nota03 = float(input('Insira a terceira nota: '))

lista_notas = []

lista_notas.append(nota01) 
lista_notas.append(nota02)
lista_notas.append(nota03)

calculo = 0

for calculo in lista_notas:
    
    calculo = (nota01 + nota02 + nota03)/3
    print(calculo)
    break
