'''11. Escreva um programa que, dado o raio de um círculo, calcule a sua área e o perímetro.
A área é a superfície do objeto, dada por 3,14 multiplicados pelo raio elevado ao
quadrado. O perímetro é a medida do contorno do objeto dado por 2 multiplicados
por 3,14, multiplicados, novamente, pelo raio.'''

# Recebe o raio
raio = float(input("informe o raio\n"))

# Calculos conforme informado no exercício
area = 3.14 *raio **2
perimetro = 2 * 3.14 * raio

# Imprime o resultado
print("a area é", area)
print("o perimetro é:", perimetro)


