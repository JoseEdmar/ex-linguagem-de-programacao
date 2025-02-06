'''8. Considere uma aplicação que necessita de um calendário embutido. Assim sendo,
construa um programa que, dado um número inteiro, informe o mês correspondente,
por extenso.'''

# Lista com os meses do ano
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita um número ao usuário
num = int(input("Digite um número: "))

# Verifica se o número está dentro do intervalo válido
if 1 <= num <= 12:
    print(f"O mês correspondente é {meses[num - 1]}")
else:
    print("Digite um número de 1 a 12")
