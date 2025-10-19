'''Construa um programa que efetue a leitura das quatro notas de 20 alunos, calcule e 
mostre a média de cada aluno e a média da turma.'''

turma = []
soma_medias_turma = 0

for i in range(1, 21):
    aluno = {}
    aluno['nome'] = input(f"Digite o nome do {i}° aluno: ")
    aluno['notas'] = []
    
    for j in range(1, 5):
        nota = float(input(f"Digite a {j}° nota do aluno {aluno['nome']}: "))
        aluno['notas'].append(nota)
    
    turma.append(aluno)

print("\n--- Médias individuais ---")
for aluno in turma:
    media_aluno = sum(aluno['notas']) / len(aluno['notas'])
    soma_medias_turma += media_aluno
    print(f"A média do aluno {aluno['nome']} é {media_aluno:.2f}")

media_turma = soma_medias_turma / len(turma)

print(f"\nA média da turma é: {media_turma:.2f}")
