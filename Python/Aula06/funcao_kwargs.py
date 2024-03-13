def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")
    
mostrar_info(nome = "João", idade = 30, cidade = "Exemplo") #Isso imprimirá informações formatadas