numero_secreto = 42
numero_usuario = 0
numero_tentativas = 0

while numero_usuario != numero_secreto and numero_tentativas <3:
  numero_usuario = int(input("Digite o numero secreto:"))
  numero_tentativas += 1
  
if numero_usuario == numero_secreto:
  print("Parabéns! Você acertou o número secreto.")
else: 
  print("Você estourou o numero de tentativas.")
