def cadastrar_tarefa(nome_tarefa, descricao_tarefa, prioridade_tarefa):
    dict_tarefa = dict()
    dict_tarefa["nome"] = nome_tarefa
    dict_tarefa["descrica"] = descricao_tarefa
    dict_tarefa["prioridade"] = prioridade_tarefa
    lista_tarefa.append(dict_tarefa)
    print("Tarefa cadastrada com sucesso!!!")


lista_tarefa =[]
while True:
    print("<---------------------Bem vindo ao TaskScheduler------------------------->")
    print("Selecione as opções abaixo: ")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefa")
    print("3 - Exibir por prioridade")
    print("0 - Sair")
    opcao_menu = int(input())
    if opcao_menu == 0:
        break
    elif opcao_menu == 1:
        nome_tarefa = input("Digite o nome da tarefa: ")
        descricao_tarefa = input("Informe a descrição da tarefa: ")
        prioridade_tarefa = input("Defina a prioridade da tarefa: ")
        cadastrar_tarefa(nome_tarefa, descricao_tarefa, prioridade_tarefa)    
    elif opcao_menu == 2:
        print(lista_tarefa)
    elif opcao_menu == 3:
        lista_ordenada = sorted(lista_tarefa, key=lambda x: x["prioridade"])
        print(lista_ordenada)
