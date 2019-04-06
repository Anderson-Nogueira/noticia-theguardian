#Programa para inserir termos diferentes a uma lista 

#[] é uma vetor (lista)
#{} é um dicionário

lista_dados = [5, 7, 11, 23, 0]
minha_lista = []

print("Lista de dados Original: ", lista_dados)

cont=0
teste=0

while cont < 5:

    try:
        n1 = int(input("Entre com novos numeros: "))
    except:
        print("Favor digitar apenas números !!!")
    
    minha_lista.append(n1)
    cont = cont + 1

for elemento in minha_lista:
    if elemento not in lista_dados:
        lista_dados.append(elemento)


print("Lista de dados após inserção: ", lista_dados)

