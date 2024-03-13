# utilize uma funcao map para retornar uma nova lista contendo o dobro de cada numero de uma lista de entrada do usuario.
# solicite numeros ate o usuario digitar -1.

lista_numeros=[]
while True:

    numero = int(input("Digite um numero ou -1 para sair: "))
    if numero == -1:
        break
    else:
        lista_numeros.append(numero)
    
lista_dobro = list(map(lambda x : x*2, lista_numeros))
print(lista_dobro)