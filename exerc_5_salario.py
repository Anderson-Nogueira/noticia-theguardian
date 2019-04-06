# Programa para Calcular Salarios e Impostos

import math # importa biblioteca matemática


nome_fun = input("Entre com o nome do funcionario: ")
val_hora = float(input("Entre com o valor da sua Hora de Trabalho: "))
hs_trab = float(input("Entre com a quantidade de horas trabalhadas: "))

sal_bruto = val_hora * hs_trab
irpf = sal_bruto * 11/100
inss = sal_bruto * 8/100
sindcato = sal_bruto * 5/100

sal_liq = sal_bruto - irpf - inss - sindcato

print("Funcionário: ", nome_fun)
print("Salario Bruto: %.2f" %sal_bruto)
print("Desconto IRPF: %.2f" %irpf)
print("Desconto INSS: %.2f" %inss)
print("Salario Liquido: %.2f" %sal_liq)

