'''7. Em algumas situações, em uma aplicação, é preciso determinar quais são os números
múltiplos de um ou mais valores, dentre todos os valores de um conjunto
de dados. Dessa forma, faça um programa que receba, do usuário, um número e
informe se ele é divisível por três ou por sete.'''

num = int(input("Dígite um número: "))

if num % 3 == 0 and num % 7 == 0:
  print("O número é divisível por 3 e por 7.")
elif num % 3 == 0:
  print("o número é divisível por 3")
elif num % 7 == 0:
  print("O número é divisível por 7")
else:
  print("O número não é divisível por 3 ou 7")