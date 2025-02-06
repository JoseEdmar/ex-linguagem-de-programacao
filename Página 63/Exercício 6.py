'''6. É comum, em uma aplicação, ter de determinar quais números são o maior ou o
menor, dentre todos os valores de um conjunto de dados informados pelo usuário.
Assim sendo, escreva um programa que receba cinco números inteiros e apresente
o maior e o menor entre todos eles.'''

num1 = int(input("Digite o 1° numero"))
num2 = int(input("Digite o 2° numero"))
num3 = int(input("Digite o 3° numero"))
num4 = int(input("Digite o 4° numero"))
num5 = int(input("Digite o 5° numero"))

numeros = [num1, num2, num3, num4, num5]


print("O mair número é:", max(numeros) ,"o menor é", min(numeros))
