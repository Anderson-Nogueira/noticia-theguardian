# Programa para Dar saudações

import math # importa biblioteca matemática

try:
    fat_num = int(input("Entre com um número para Fatorial: "))
except:
    print("Entre somente números inteiros !!!")

conta=0
resultado=1
volta=fat_num

while conta < volta:
    resultado=resultado*fat_num
    conta = conta + 1
    fat_num = fat_num - 1
    
print("O resultado da Fatoração é: ", resultado)
    
