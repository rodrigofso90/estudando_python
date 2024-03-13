# dados_usuario = {
#     'nome': 'Raama',
#     'idade': 18,
#     'cidade': 'salvador'
# }

# print(dados_usuario)


lista_compras = {
    'leite': 5.20,
    'café': 9.20,
    'biscoito': 12.20
}

# print(lista_compras['leite'])
# print(lista_compras.get('café'))

for chave in lista_compras:
    print(chave)
    # print(lista_compras[chave])
    print(lista_compras.get(chave))