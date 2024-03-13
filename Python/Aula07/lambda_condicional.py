def realiza_operacao(operacao,numero1, numero2):
    return operacao(numero1, numero2)

print(realiza_operacao(lambda x,y : + x+y, 1, 5))


# par_impar = lambda x : "Par" if x % 2 == 0 else "impar"

# print(par_impar(2))
# print(par_impar(3))