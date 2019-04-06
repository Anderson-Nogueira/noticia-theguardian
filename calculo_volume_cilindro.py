# Programa para saber o numero de dias de vida de uma pessoa

import math # importa biblioteca matemática

print("Programa P/ Cálculo do Cilíndro !!!")

try:
    raio = float(input("Entre com o raio do cilíndro: "))
    altura = float(input("Entre com a altura do cilíndro: "))
except:
    print("Digite apenas números !!!")

volume = math.pi * raio**2 * altura

print("O volume do cilíndro é %.2f" % volume, "m3")
