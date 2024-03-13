#crie um programa para organizar uma lista de compras
#crie uma lista vazia
# Solicite ao usuario os nomes dos produtos e adicione na lista
# Quando o usuario digitar 3, saia do programa e imprima a lista

lista_compras = []

while True:
    opcao = int(input("Insira a opção desejada:\n 1 para adicionar.\n 2 para remover.\n 3 para sair. \nAguardando opção desejada: "))
    if opcao == 1:
        input("Digite o alimento desejado para adicionar: ")
        lista_compras.append(opcao)
    elif opcao == 2:
        remove_alimento = input("Digite o alimento desejado para remover: ")
        if lista_compras == remove_alimento:
            lista_compras.remove(lista_compras)
        else:
            print("Erro insira novamente")
            continue
    else:
        print("Saindo do programa...")
        break
    
    
print(lista_compras)


# lista_compras = []

# while True:
#     nome_produto = input("Digite o nome do produto ou digite 3 para sair.")
#     if nome_produto == "3":
#         break
#     else:
#         lista_compras.append(nome_produto)
# print(lista_compras)