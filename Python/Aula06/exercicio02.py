# Crie uma função que receba um horário e imprima "Bom dia!", "Boa tarde!" ou "Boa Noite" conforme o horário.
# a função vai receber um numero inteiro de 0 a 24.

# de 0 até 5 é noite
# de 6 até 12 é dia
# de 13 até 18 é tarde
# de 19 até 24 é noite

def saudacao(hora):
        if  hora >= 0 and hora <=5:
            print("Boa noite!")
        elif hora >= 6 and hora <= 12:
            print("Bom dia!")
        elif hora >= 13 and hora <= 18:
            print("Boa Tarde!")
        elif hora >=19 and hora <= 24:
            print("Boa Noite!")
        else:
            print("Digite a hora correta!!!")


info_hora = int(input("Informe a hora: "))

saudacao(info_hora)
