# Programa para saber qual numero é maior

import math # importa biblioteca matemática


n1 = int(input("Entre com o primeiro numero: "))
n2 = int(input("Entre com o segundo numero: "))
n3 = int(input("Entre com o terceiro numero: "))

if (n1>n2) and (n1>n3):
    print("O primeiro número é o maior !!!")
elif (n2>n1) and (n2>n3):
    print("O segundo número é o maior !!!")
elif (n3>n1) and (n3>n2):
    print("O terceiro número é o maior !!!")

