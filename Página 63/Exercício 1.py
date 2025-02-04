# 1. Faça um programa que leia um número e informe se ele é divisível por cinco.

# Recebe o número
num = int(input("Dígite um número: "))

# Verifica divisibilidade por 5
if num % 5 == 0:
  print("o número é divisível por 5")
else:
  print("O número não é divisível por 5")