'''5. Faça um programa que receba o valor de um depósito e o valor da taxa de juros,
calcule e apresente o valor do rendimento e o valor total (valor do depósito + valor
do rendimento).'''

# Recebe os valores digitados pelo usuário
valor_deposito = float(input("Dígite um valor para depósito\n"))
taxa_juros = float(input("Dígite a taxa de juros\n"))

# Faz o cálculo de juros
rendimento = valor_deposito * taxa_juros

# Imprime o resultado
print("O valor do rendimento é:", valor_deposito, "o valor total é:", rendimento + valor_deposito)