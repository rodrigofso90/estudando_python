# crie um set para guardar sua lista de mercado
# solicite ao usuario para digitar os itens de mercado
# até que ele digite 2. Quando ele digitar 2, saia do programa

lista_mercado = set([])

while True:
    opcao = int(input("Insira a opção desejada:\n 1 para adicionar.\n 2 para sair. \nAguardando opção desejada: "))
    if opcao == 1:
        opcao = input('Digite o produtor que deseja adicionar: ')
        lista_mercado.add(opcao)
    if opcao == 2:
        print('Saindo...')
        break
        
        
print(lista_mercado)