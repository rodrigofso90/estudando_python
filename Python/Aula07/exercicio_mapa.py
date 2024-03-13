lista_precos = [40.0, 20.5, 30.5]

# Crie uma lista_precos_com_desconto aplicando 10 % de desconto aos itens. Utilize o map
# ex:
# quadrados = list(map(lambda x:x**2, lista))
# print(quadrados)

lista_precos_com_desconto = list(map(lambda x : x*10/100, lista_precos))
print(lista_precos_com_desconto)