def somar_numeros (*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado


print(somar_numeros(1, 2, 3)) #imprime o valor "6"
print(somar_numeros(10, 20, 30, 40, 50)) #imprime o valor "150"