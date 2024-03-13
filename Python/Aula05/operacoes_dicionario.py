computador = {'cpu':'intel', 'Ram':'8GB','SSD':'250GB'}

inter_computador = iter(computador)

print(next(inter_computador))
print(next(inter_computador))
print(next(inter_computador))

print("-----------FOR---------")

for chave in computador:
    print(chave, '= ', computador[chave])