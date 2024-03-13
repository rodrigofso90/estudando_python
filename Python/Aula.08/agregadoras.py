#map, filter, reduce

frutas = ['Uva', 'Banana', 'Goiaba', 'Tangerina']

frutas_M = map(lambda f: f.upper(), frutas )
print(frutas_M)


from functools import reduce

idades = [18, 60, 35, 35, 6, 14]

soma = 0
for item in idades:
    soma = soma + item

soma = reduce(lambda soma, item: soma + item, idades )
print(soma)