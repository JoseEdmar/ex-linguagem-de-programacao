lista_A = []
lista_B = []


print("Dígite 20 números para a lista A")
for i in range(1, 21):
    numero = int(input(f"Dígite o {i}° número da lista A\n"))
    lista_A.append(numero)

print("Dígite 20 números para a lista B")
for i in range(1, 21):
    numero = int(input(f"Dígite o {i}° número da lista B\n"))
    lista_B.append(numero)

lista_C = [a + b for a, b in zip(lista_A, lista_B)]

print(f"A lista reversa é: {lista_C}")