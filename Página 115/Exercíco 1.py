'''Escreva um programa que leia uma lista com um total de 30 elementos numéricos 
do tipo inteiro. Em seguida, apresente a mesma lista impressa em ordem inversa 
à ordem de entrada.'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

lista_inversa = lista[:: -1]

print(f"A lista inversa é: {lista_inversa}")