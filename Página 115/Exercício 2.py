'''Faça um programa que leia duas listas A e B, ambas com 20 números inteiros. Efetue 
a soma entre as duas listas em uma terceira lista C e imprima C em ordem crescente.'''
lista_A = []
lista_B = []


print("Dígite 20 números para a lista A")
for i in range(1, 21):
    numero1 = int(input(f"Dígite o {i}° número da lista A\n"))
    lista_A.append(numero1)

print("Dígite 20 números para a lista B")
for i in range(1, 21):
    numero2 = int(input(f"Dígite o {i}° número da lista B\n"))
    lista_B.append(numero2)

lista_C = [a + b for a, b in zip(lista_A, lista_B)]
lista_C.sort()

print(f"Lista ordenada e somada: {lista_C}")