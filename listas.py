#Programa para estudo de lista de dados / dicionários

#[] é uma vetor (lista)
#{} é um dicionário

lista_dados = [31, 1.80, "Python", ['C', 'A', 'O'], True, False]
print(lista_dados[2])
print(lista_dados[3][1])

lista_dicionarios = [{"fruta": "uva", "cor": "verde"}, {"fruta": "maracuja", "cor": "amarelo"}, {"fruta": "acerola", "cor": "vermelha"}]
print(lista_dicionarios[1]["fruta"])

#Adicionando elementos em uma lista
lista_nomes = ["João", "Pedro", "Maria"]
print(lista_nomes)

# insere um registro no final
lista_nomes.append("José")
print(lista_nomes)

# insere um registro na posição desejada
lista_nomes.insert(1,"Marcos")
print(lista_nomes)

# apaga um registro na última posição
lista_nomes.pop()
print(lista_nomes)

# apaga um registro na posição desejada
lista_nomes.pop(1)
print(lista_nomes)

# Coloca a lista de trás para frente
lista_nomes.reverse()
print(lista_nomes)

# Coloca a lista em ordem alfabética ou numérica
lista_nomes.sort()
print(lista_nomes)

# remove a primeira ocorrência de um determinado elemento da lista
lista_nomes.remove("Pedro")
print(lista_nomes)

# Conta a quantidade de ocorrências de um determinado elemento elementos
print(lista_nomes.count("Maria"))

#CRIACAO DE LISTA NUMÉRICA
lista_idades = [4, 50, 24, 39, 10]

#sabendo a quantidade de elementos da lista
print(len(lista_idades))
