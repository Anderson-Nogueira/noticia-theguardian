#Programa para inserir termos diferentes a uma lista 

#[] é uma vetor (lista)
#{} é um dicionário

lista_dados = [5, 7, 11, 23, 0]
print("Lista de dados Original: ", lista_dados)

cont=0
teste=0

try:
    teste = int(input("Quantos numeros serão testados? "))
except:
    print("Entre somente números inteiros !!!")

while cont < teste:

    try:
        n1 = int(input("Entre com novos numeros: "))
    except:
        print("Favor digitar apenas números !!!")
    
    verifica=lista_dados.count(n1)
   
    if verifica == 0:
       lista_dados.append(n1) 
    
    cont = cont + 1

print("Lista de dados após inserção: ", lista_dados)

