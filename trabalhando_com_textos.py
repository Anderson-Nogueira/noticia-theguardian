#Programa Para Trabalhar com STRINGS

import math
import datetime

nome = "Curso de Python"
datas = "31/03/2019"

datas_isoladas = datas.split("/") #split quebra em vetor os termos da varíavel, pelo caracter informado
print(datas_isoladas)

nome_isolado = nome.split(" ")
print(nome_isolado)
print(nome_isolado[1]) #printa o termo "1" do vetor

d="2019-03-31"
print("%s / %s / %s" % (d[8:],d[5:7],d[0:4])) 

