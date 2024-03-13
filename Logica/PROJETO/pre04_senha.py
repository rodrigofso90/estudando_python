# Após ligar o celular, é necessário inserir a senha cadastrada.

# São 3 tentativas até o telefone bloquear.

# Se o usuário acertar a senha, escreva a mensagem:“bem vindo.”

# Se o usuário errar a senha, escreva a mensagem: “Senha incorretar. Você tem x tentativas até o bloqueio.


senha_correta = 123456

tentativa = 3

for i in range(1,4):
    senha = int(input("Insira a senha: "))  
    if senha == senha_correta:
        print("Bem vindo!")
        break
    else:
        tentativa = tentativa -1
        if tentativa == 0:
            print(f"Você nao tem mais tentativas")
        else:
            print(f"Tente novamente, você possui {tentativa} tentativas")