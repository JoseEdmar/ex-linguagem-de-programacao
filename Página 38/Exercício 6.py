'''6. Escreva um programa que receba dois números, calcule e apresente o resultado do
primeiro número elevado ao segundo.'''

# Recebe os números
num1 = float(input("Dígite um número\n"))
num2 = float(input("Dígite outro número\n"))

# Eleva o 1º número ao 2º
elevado = pow(num1, num2)

# Imprime o resultado
print(num1, "Elevado a", num2, "é:", elevado)
