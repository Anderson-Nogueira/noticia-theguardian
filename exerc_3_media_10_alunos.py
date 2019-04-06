# Programa para Ler notas de 10 alunos e depois dar a média

import math # importa biblioteca matemática


try:
    qtd_alunos = int(input("Quantos Alunos Serão Analisados? "))
except:
    print("Entre somente números inteiros !!!")

conta=0
notas=0
ent_notas=0
media=[]
media_calc=0
alunos=[]
ent_alunos=""

n_nota=0

while conta < qtd_alunos:
    
    ent_alunos=input("Entre com o nome do Aluno: ")
    alunos.append(ent_alunos)

    while n_nota < 4:
        ent_notas=float(input("Entre com a Nota: "))
        notas=ent_notas + notas
        n_nota = n_nota + 1
 #       print(ent_notas)
    
    media_calc=notas/4
    media.append(media_calc)

    ent_notas=0
    n_nota=0
    notas=0
    conta=conta + 1

conta=0

while conta < qtd_alunos:
    
    print("Aluno: ", alunos[conta], " Teve média de ", media[conta])
    conta = conta + 1

