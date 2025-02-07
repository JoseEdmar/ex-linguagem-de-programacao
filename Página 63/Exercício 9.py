'''9. Elabore um programa que receba o salário de um funcionário e o código do cargo e
apresente o cargo, o valor do aumento e o novo salário. A tabela a seguir apresenta
os respectivos código, cargo e percentual do aumento para cada tipo de colaborador.
Código Cargo Percentual do aumento
1 Servente 40%
2 Pedreiro 35%
3 Mestre de obras 20%
4 Técnico de segurança 10%'''

salario = float(input("Informe o seu salário: R$"))
codigo = int(input("Informe o seu código "))

if codigo == 1:
  cargo = "Servente"
  aumento = salario * 0.40
elif codigo == 2:
  cargo = "Pedreiro"
  aumento = salario * 0.35
elif codigo == 3:
  cargo = "Mestre de obras"
  aumento = salario * 0.20
elif codigo == 4:
  cargo = "Técnico de segurança"
  aumento = salario * 0.10

novo_salario = aumento + salario

print("Seu cartgo é:", cargo)
print("Seu aumento foi de: R$", aumento)
print("Seu novo salário:", novo_salario)
