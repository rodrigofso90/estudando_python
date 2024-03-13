# Crie uma função chamada concatenar_strings que aceita um numero variavel de strings como argumentos posicionais (usando *args). A função deve concatenar
# todas as strings em uma unica string e retorna-la. Chame a funcao 3 vezes passando diferente quantidades de argumentos
# ex:
# concatenar_strings("olá", "Paschoal")
# concatenar_strings("Bom", "dia", "seja","Bem","Vindo")
# concatenar_strings(" ", "Wolrd","!")

from functools import reduce

def concatenar_strings(*args):
    resultado = ""
    for palavra in args:
        resultado = resultado + " " + palavra
    return resultado


print(concatenar_strings("olá", "Paschoal"))
print(concatenar_strings("Bom", "dia", "seja","Bem","Vindo"))
print(concatenar_strings("Hello", "Wolrd","!"))
