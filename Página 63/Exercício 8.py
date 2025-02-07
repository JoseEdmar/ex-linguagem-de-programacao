'''8. Considere uma aplicação que necessita de um calendário embutido. Assim sendo,
construa um programa que, dado um número inteiro, informe o mês correspondente,
por extenso.'''

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

num = int(input("Digite um número: "))

if 1 <= num <= 12:
  print(f"O mês correspondente é: {meses[num - 1]}")
