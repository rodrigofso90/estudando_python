senha_correta = 123456

tentativa = 0

while True:
    tentativa = tentativa + 1
    senha = int(input("Insira a senha: "))
    if senha_correta == senha:
        print(f"Senha está correta!")
        break
    else:
        print(f"Senha está incorreta, insira novamente!")
        if tentativa == 3:
            print("Você tentou 3 vezes. bloqueando o programa...")
            break


