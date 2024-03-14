# dict = {}
# lista de tarefas contendo informações pessoais
lista_informacoes =  {"nome":"nome",
                      "descricao":"descricao",
                      "prioridade":"prioridade",
                      "categoria":"categoria"
                      }

lista_informacoes_2 = {

}
# # Funções
def adicionar_tarefas():
    lista_adicionar_tarefas = []

# def listar_tarefas():

# def marcar_concluidas():

# def exibir_tarefas():

while True:
    opcoes = int(input("Informe a opção desejada:\n 1 - Adicionar Tarefa\n 2 - Listar Tarefas\n 3 - Marcar como concluida\n 4 - Exibir Tarefa\n 5 - Sair.\n Aguardando opção: "))

    if opcoes == 1:
        adicionar_tarefas()



