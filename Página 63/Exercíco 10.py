'''10. Faça um programa que receba o código do estado de origem da carga de um caminhão,
o peso da carga em toneladas e o código dela.
Código do estado Taxa de imposto
1 20%
2 15%
3 10%
4 5%
Código da carga Preço por quilo
10 a 20 180
21 a 30 120
31 a 40 230'''

cod_estado = int(input("Digite o código do estado (1 a 4):\n"))
peso = int(input("Digite o peso da carga em toneladas:\n"))
cod_carga = int(input("Digite o código da carga (10 a 40):\n"))


if cod_estado == 1:
    taxa_imp = 0.2
elif cod_estado == 2:
    taxa_imp = 0.15
elif cod_estado == 3:
    taxa_imp = 0.1
elif cod_estado == 4:
    taxa_imp = 0.05



if 10 <= cod_carga <= 20:
    valor_carga = 180
elif 21 <= cod_carga <= 30:
    valor_carga = 120
elif 31 <= cod_carga <= 40:
    valor_carga = 230


kg = peso * 1000
valor = kg * valor_carga
imposto = valor * taxa_imp
valor_total = valor + imposto


print("Peso em quilos:", kg)
print("Valor da carga: R$", valor)
print("Imposto: R$", imposto)
print("Valor total com imposto: R$", valor_total)
