# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.

notas_equipe_1 = ('Equipe Mascote',[7,2,3,5])
notas_equipe_2 = ('Equipe Falcao',[8,7,9,2])
notas_equipe_3 = ('Equipe Bel Marques',[6,2,1,3])


lista_medias = []

soma_notas = 0
for item in notas_equipe_1[1]:
    soma_notas += item
    
media_1 = soma_notas /len(notas_equipe_1[1])
lista_medias.append(media_1)

soma_notas = 0
for item in notas_equipe_2[1]:
    soma_notas += item
    
media_2 = soma_notas /len(notas_equipe_2[1])
lista_medias.append(media_2)

soma_notas = 0
for item in notas_equipe_3[1]:
    soma_notas += item
    
media_3 = soma_notas /len(notas_equipe_3[1])
lista_medias.append(media_3)
print(lista_medias)


