# lista_numeros = [2,3,5,6,7,8,9,10]

# #Utilizando um filter, filtre todos os números impares

# #A partir dessa lista de impares, multiplique todos os numeros por 3

# # A partir da ultima lsita, execute a soma de todos os numeros


# Ex: filter
# lista = list(filter(lambda x : x %2 ==0, numeros))

# reduce
# #soma =  reduce(lambda x,y : x+y,numeros)

# mapa
# #quadrados = list(map(lambda x : x **2,lista))

from functools import reduce


lista_numeros = [2,3,5,6,7,8,9,10]

lista_impares = list(filter(lambda x : x%2 != 0, lista_numeros))

lista_impares_mult_3 = list(map(lambda x:x *3, lista_impares))

soma = reduce(lambda x,y: x+y, lista_impares_mult_3)

print(soma)
