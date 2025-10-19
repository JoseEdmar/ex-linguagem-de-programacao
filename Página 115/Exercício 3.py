'''Faça um programa que leia um nome e apresente as letras que se encontram nas 
posições pares.'''

nome = input("Dígite um nome: ")

letra_par = nome [1::2]

if len(letra_par) > 1:
    print(f"As letras pares são: {letra_par}")
else:
    print(f"A letra par é: {letra_par}")