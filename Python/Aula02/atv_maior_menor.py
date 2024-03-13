num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))


if num1 > num2:
  print(f"O maior é o primeiro numero: {num1}")
elif num1 < num2:
    print(f"O segundo numero é maior: {num2}")
else:
    print("os numero são iguais.")