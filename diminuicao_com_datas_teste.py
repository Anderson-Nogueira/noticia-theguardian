#Programa Para Trabalhar com STRINGS

import math
import datetime


dt1 = "28/03/2019"
dt1_isolado = dt1.split("/")
dt2 = "31/03/2019"
dt2_isolado = dt2.split("/")

print(dt1_isolado)
print(dt2_isolado)

print(int(dt1_isolado[2]))

print(datetime.date(int(dt2_isolado[2]), int(dt2_isolado[1]), int(dt2_isolado[0])))
print(datetime.date(int(dt1_isolado[2]), int(dt1_isolado[1]), int(dt1_isolado[0])))

qtd_dias = datetime.date(int(dt2_isolado[2]), int(dt2_isolado[1]), int(dt2_isolado[0])) - datetime.date(int(dt1_isolado[2]), int(dt1_isolado[1]), int(dt1_isolado[0]))

print("Quantidade de dias", str(qtd_dias))


#Testando Agora com Entrada de Datas

print("--------------- Entrando com as DATAS ------------------------")

dt1 = input("Entre com a primeira Data: ")
dt2 = input("Entre com a segunda Data: ")

#dt1 = "28/03/2019"
dt1_isolado = dt1.split("/")
#dt2 = "31/03/2019"
dt2_isolado = dt2.split("/")

print(dt1_isolado)
print(dt2_isolado)

print(int(dt1_isolado[2]))

print(datetime.date(int(dt2_isolado[2]), int(dt2_isolado[1]), int(dt2_isolado[0])))
print(datetime.date(int(dt1_isolado[2]), int(dt1_isolado[1]), int(dt1_isolado[0])))

qtd_dias = datetime.date(int(dt2_isolado[2]), int(dt2_isolado[1]), int(dt2_isolado[0])) - datetime.date(int(dt1_isolado[2]), int(dt1_isolado[1]), int(dt1_isolado[0]))

print("Quantidade de dias", str(qtd_dias))
