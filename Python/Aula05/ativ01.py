
# Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve
# permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os
# resultados finais.

# candidatos = {"Rodrigo":0, "Adriano":0, "Bruno":0}
# eleicao = dict()

# print(f"Numero de votos de cada candidato:\n{candidatos}\n")

# while True:
#     voto = int(input("Digite o nome do seu candidato:\nRodrigo\nAdriano\nBruno\n0 - Verificar quantidade de votos\n"))
    
#     if voto == 1:
#         candidatos[voto] = 
    
#     break

dict_candidatos = {'Tiririca':0, 'Toin':0}

while True:
    print("Bem vindo ao sistema ao sistema eletronico de votacao")
    print("Selecione um candidato entre os seguintes:")
    print(list(dict_candidatos))
    candidatos_escolhido = input("Digite: ")
    if candidatos_escolhido == '0':
        break
    dict_candidatos[candidatos_escolhido] = dict_candidatos[candidatos_escolhido] + 1

print(dict_candidatos)

# dict_candidatos = {'Tiririca':0,'Toin':0}

# while True:
#     print("Bem vindo ao sistema eletrônico de votação")
#     print("Selecione um candidato entre os seguintes:")
#     print(list(dict_candidatos))
#     candidato_escolhido = input('Candidato:')
#     if candidato_escolhido == '0':
#         break
#     dict_candidatos[candidato_escolhido] = dict_candidatos[candidato_escolhido] + 1

# print(dict_candidatos)