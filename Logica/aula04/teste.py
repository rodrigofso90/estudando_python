# for(let i = 0;i<10;i++){
#     print(i)
# }

# for i in range(0,11):
#     print("")
#     print(f"Imprimindo o i {i}")
#     print("*"*30)
#     for j in range(0,5):
        
#         print(f"Imprimindo o j {j}")



# nome = "victor"
# for i in nome:

#     if i == "t":
#         print(f"Você vai imprimir o texto 't', encerrando... ")
#         continue
#     print(i)

# for i in range(5):
#     print(i)

# for num in range(2,20):
#     for i in range(2,num):
#         if num%i == 0:
#             break
#     else:
#         print(f"{num} é primo")


# preco = float(input('Digite o preço do pão: '))
# print('Preço do pão: R$ %.2f' % preco)
# print('Panificadora Pão de Ontem - Tabela de preços')
# valor = preco
# for i in range(1, 51):
#     print('%d - R$ %.2f' %(i, valor))

#     valor += preco


# maiorAcidente = 0
# maiorAcidenteCidade = 0

# menorAcicendte = 0
# menorAcidenteCidade = 0

# somaVeiculos = 0
# somaAcidentes = 0
# countAcicentes = 0
# for i in range(1, 6):
#     codigo = int(input('Digite o código da cidade: '))
#     veiculos = int(input('Digite o número de veículos de passeio(em 1999): '))
#     acidentes = int(input('Digite o número de acidentes de trânsito com vítimas(em 1999): '))

#     if i == 1:
#         menorAcidente = acidentes
#         menorAcidenteCidade = codigo
        
#     if acidentes > maiorAcidente:
#         maiorAcidente = acidentes
#         maiorAcidenteCidade = codigo
        
#     if acidentes < menorAcidente:
#         menorAcidente = acidentes
#         menorAcidenteCidade = codigo

#     somaVeiculos += veiculos

#     if veiculos < 2000:
#         somaAcidentes += acidentes
#         countAcicentes += 1

# print('Maior índice de acidentes de trânsito')
# print('%d acidentes na cidade %d' %(maiorAcidente, maiorAcidenteCidade))

# print('Menor índice de acidentes de trânsito')
# print('%d acidentes na cidade %d' %(menorAcidente, menorAcidenteCidade))

# print('Média de veículos das cinco cidades: %.2f' %(somaVeiculos/5))
# print('média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: %.2f' %(somaAcidentes/countAcicentes))
    