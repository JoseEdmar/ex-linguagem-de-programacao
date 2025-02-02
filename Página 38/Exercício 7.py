# 7. Elabore um programa que calcula a área de um trapézio.

# Recebe os valores
base1 = float(input("Digite o tamanho da base: "))
base2 = float(input("Digite o tamanho da outra base: "))
altura = float(input("Digite a altura do trapézio: "))

# Cálculo da área
soma_das_bases = base1 + base2  
area = (soma_das_bases * altura) / 2

# Imprime o resultado
print("A área do trapézio é:", area)
