# Programa para Dar saudações

import math # importa biblioteca matemática

vdd = "N"

while vdd == "N":

    turno = str(input("Em que turno vc estuda? ")).upper()
    
    if (turno=="M") or (turno=="V") or (turno=="N"):
        if (turno=="M"):
            print("Bom Dia !!!")
            vdd="S"
        elif (turno=="V"):
            print("Boa Tarde !!!")
            vdd="S"
        elif (turno=="N"):
            print("Boa Noite !!!")
            vdd="S"
    else:
        print("Digite apenas: M-> Matutino, V->Vespertino ou N->Noturno !!!")
    
