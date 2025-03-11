'''3. Construa um programa que receba a idade de uma pessoa e identifique sua classe
eleitoral: não eleitor (menor que 16 anos de idade), eleitor obrigatório (entre 18 e
65 anos) e eleitor facultativo (entre 16 e 18 e maior que 65).'''

idade = int(input("Qual a sua idade?"))

if idade < 16:
  print("Não eleitor")
elif idade >= 18 and idade <= 65:
  print("Eleitor obrigatório")
elif idade >= 16 and (idade < 18 or idade > 65):
  print("Eleitor Facultativo")
  