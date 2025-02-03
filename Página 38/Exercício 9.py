'''9. Escreva um programa que leia um número positivo inteiro e apresente o quadrado
e a raiz quadrada desse número.'''

# Importa a bíbloiteca Math 
import math

# Solicita ao usuário um número inteiro
num = int(input("Dígite um número inteiro\n"))

# Calcula a raiz quadrada do número
raiz = math.sqrt(num) 

# Calcula ao quadrado
num = num * num

# Imprime o resultado na tela
print("O número ao quadrado é:", num ,"e a raiz quadrada é:", raiz)