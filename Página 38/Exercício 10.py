'''10. Escreva um programa que receba três números e seus respectivos pesos, calcule e
apresente a média ponderada entre eles. Observação: a média pode ser um dado
numérico com casas decimais, portanto, prepare seu programa para que ele seja
capaz de apresentar o resultado apropriado, quando necessário.'''

num1 = float(input("Digite um número: "))
p1 = float(input("Digite um peso para o 1° número: "))
num2 = float(input("Digite um número: ")) 
p2 = float(input("Digite um peso para o 2º número: "))
num3 = float(input("Digite um número: "))
p3 = float(input("Digite um peso para o 3° número: "))

soma_pesos = p1 + p2 + p3

if soma_pesos == 0:
    print("Erro: A soma dos pesos não pode ser zero.")
else:
    media = (num1 * p1 + num2 * p2 + num3 * p3) / soma_pesos
    print("A média ponderada é:", round(media, 2))
