'''2. Elabore um programa que receba o nome e a idade de uma pessoa e informe o
nome, a idade e o valor da mensalidade do plano de saúde. A tabela a seguir apresenta
os valores de mensalidade com base na faixa etária.
Até 18 anos R$ 50,00
De 19 a 29 anos R$ 70,00
De 30 a 45 anos R$ 90,00
De 46 a 65 anos R$ 130,00
Acima de 65 anos R$ 170,00'''

# Recebe as informações
nome = str(input("Qual é o seu nome? "))
idade = int(input("Quantos anos você tem? "))

# Imprime a resposta correspondente a idade
if idade <=18:
  print("Nome:", nome,".", idade,"Anos,", "Valor do plano de saúde R$ 50,00")
elif idade >= 19 and idade <= 29:
  print("Nome:", nome,".", idade,"Anos,", "Valor do plano de saúde R$ 70,00")
elif idade >= 30 and  idade <=45:
  print("Nome:", nome,".", idade,"Anos,", "Valor do plano de saúde R$ 90,00")
elif idade >= 46 and idade <= 65:
  print("Nome:", nome,".", idade,"Anos,", "Valor do plano de saúde R$ 130,00")
else:
  print("Nome:", nome,".", idade,"Anos,", "Valor do plano de saúde R$170,00")



