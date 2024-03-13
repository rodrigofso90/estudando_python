

# frutas = {"Maçã", "Banana", "Cereja", "Maçã"}


# print(frutas)


# lista_numeros = ['2', '3','5']

# print(set(lista_numeros))

set_numeros = {2,3,4,5,6}
set_numeros_2 = {2,3,4,5,6,10,12,15}

set_numeros.discard(2)

set_numeros.update(set_numeros_2)

print(set_numeros)
print(len(set_numeros))