'''5. Faça um programa que informe a quantidade total de calorias a partir da escolha
do usuário, que deve informar o prato típico e a bebida. A tabela de calorias encontra-
se a seguir.
Prato Bebida
Italiano 750 cal Chá 30 cal
Japonês 324 cal Suco de laranja 80 cal
Salvadorenho 545 cal Refrigerante 90 cal'''

# Obs: também dá pra fazer só com os valores caloricos de cada prato e bebida nos if, não precisa necessariamente criar uma variavel com o nome e valor.

Italiano = 750
Japonês = 324
Salvadorenho = 545

Chá = 30
Suco_de_laranja = 80
Refrigerante = 90

calorias = 0

print("Escolha um prato típico")
print("1 - Italiano")
print("2 - Japonês")
print("3 - Salvadorenho")

op1 = int(input())


if op1 == 1:
 calorias = Italiano
elif op1 == 2:
 calorias = Japonês
elif op1 == 3:
 calorias = Salvadorenho

print("Escolha uma bebida")
print("1 - Chá")
print("2 - Suco de laranja")
print("3 - Refrigerante")

op2 = int(input())


if op2 == 1:
 calorias += Chá
elif op2 == 2:
 calorias += Suco_de_laranja
elif op2 == 3:
 calorias += Refrigerante

print("O total de calorias é:", calorias)
