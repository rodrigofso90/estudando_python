import random
 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
add_erro = 0

while True:
    advinha = int(input("Tente acerta o numero de 1 a 3: "))

    numero_randon = random.choice(list1)

    if numero_randon == advinha:
        print(f"Você acertou o numero aleatorio...{numero_randon} e {advinha}.\nVocê tentou: {add_erro}")
        break
    else:
        add_erro = add_erro + 1
        print(f"Você errou o numero...\nVocê tentou {add_erro} vezes")
        print(numero_randon)
