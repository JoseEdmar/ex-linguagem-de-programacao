'''4. De acordo com uma tabela médica, o peso ideal está relacionado com a altura e o
sexo de uma pessoa. Elabore um algoritmo que receba altura e sexo de uma pessoa
e calcule e imprima seu peso ideal, sabendo que:
a) Para homens o peso ideal é igual a 72,7 multiplicados pela altura, subtraídos
por 58.
b) Para mulheres o peso ideal é igual a 62,1 multiplicados pela altura, subtraídos
por 44,7.'''

altura = float(input("Qual sua altura em metros? "))
sexo = str(input("Qual o seu sexo? (M/F) "))
M = 72.7 * altura - 58
F = 62.1 * altura - 44.7

if sexo == "M":
  print("Seu peso ideal é:", M)
elif sexo == "F":
  print("Seu peso ideal é:", F)
else:
  print("Comando inválido")
  