# Programa para saber o numero de dias de vida de uma pessoa

import math # importa biblioteca matemática
import datetime # importa biblioteca datas

#try e except é para justamente forçar uma determinada digitação
#da erro, ele mesmo trata se não passa e mostra a msg e volta para o inicio

try:
    idade = int(input("Entre com sua Idade: "))
    meses = int(input("Entre com numero de meses: "))
except:
    print("Favor digitar apenas números !!!")

dias = idade*360 + meses*30

print("Vc possui: ", dias, "de vida")

#Testar depois cálculo com datas diretamentes

#print("---------TESTE por DATAS !!!-------------------------")

#dt_nas = input("Entre com Data de Nascimento: ")
#dt_hj = input("Entre com Data Atual: ")

#print(from datetime import datetime)

#dias2 = (datetime.strptime(dt_hj, "%d-%m-%Y") - datetime.strptime(dt_nas, "%d-%m-%Y"))

#dias2 = dt_hj - dt_nas

#print("Vc possui: ", str(dias2), "de vida")

