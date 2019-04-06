# Programa para saber qual numero é maior

import math # importa biblioteca matemática

print("Programa Para Identificar Qual numero Digitado é maior !!!")

cont=0
maior=0
menor=0

try:
    teste = int(input("Quantos numeros serão testados? "))
except:
    print("Entre somente números inteiros !!!")

while cont < teste:

    try:
        n = int(input("Entre com o número: "))
    except:
        print("Entre apenas com números inteiros !!!")
    
    if maior<n:
        maior=n

    if menor>n:
        menor=n

    cont = cont + 1

print("O menor numero foi: ", menor)
print("O maior numero foi: ", maior)
