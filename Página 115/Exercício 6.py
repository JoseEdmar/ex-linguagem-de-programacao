'''Construa um programa que efetue a leitura das quatro notas de 20 alunos, calcule e 
mostre a média de cada aluno e a média da turma.'''

alunos = []
soma_medias = 0

for i in range(1, 21):
    nome = input(f"Digite o nome do {i}° aluno: ")
    notas = []
    for j in range(1, 5):
        nota = float(input(f"Digite a {j}° nota do aluno {nome}: "))
        notas.append(nota)
    media = sum(notas) / 4
    soma_medias += media
    alunos.append({'nome': nome, 'notas': notas, 'media': media})

for aluno in alunos:
    print(f"A média de {aluno['nome']} é {aluno['media']:.2f}")

media_turma = soma_medias / 20
print(f"A média da turma é {media_turma:.2f}")

